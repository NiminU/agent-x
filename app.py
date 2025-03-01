from flask import Flask, request, jsonify, render_template
import json
import requests
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI()

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for provided coordinates in celsius.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"}
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False
        },
        "strict": True
    }
}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    messages = [{"role": "system", "content": "You are Agent X, a helpful AI assistant that can answer general questions and provide weather information."},
               {"role": "user", "content": user_message}]
    
    try:
        # First completion to check if we need to call the weather function
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools,
        )
        
        assistant_message = completion.choices[0].message
        
        # Check if the model wants to call a function
        if assistant_message.tool_calls:
            tool_call = assistant_message.tool_calls[0]
            args = json.loads(tool_call.function.arguments)
            
            # Call the weather function
            result = get_weather(args["latitude"], args["longitude"])
            
            # Append the messages for the second completion
            messages.append(assistant_message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })
            
            # Second completion to get the final response
            completion_2 = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=tools,
            )
            
            final_response = completion_2.choices[0].message.content
        else:
            # If no function was called, just use the response from the first completion
            final_response = assistant_message.content
            
        return jsonify({"response": final_response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200, debug=True)