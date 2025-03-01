# Agent X - AI Chatbot

Agent X is a Flask-based AI chatbot application that uses OpenAI's function calling capabilities to respond to user queries and provide weather information. Can be used as a template for OpenAI based chatbot with additional tool (function calling) capabilities.

## Features

- Chat interface with Agent X, a helpful AI assistant
- Get weather information for any location
- Dockerized application for easy deployment

## Prerequisites

- Docker and Docker Compose
- OpenAI API Key

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/NiminU/agent-x.git
   cd agent-x
   ```

2. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY=your-api-key
   ```

3. Build and run with Docker Compose:
   ```
   docker-compose up -d
   ```

4. Access the application in your browser:
   ```
   http://localhost:4200
   ```

## Usage

- Type your questions in the chat input field
- Ask about the weather in any location (e.g., "What's the weather like in New York?")
- Get responses from Agent X

## Running Without Docker

If you prefer to run the application without Docker:

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key:
   ```
   export OPENAI_API_KEY=your-api-key  # On Windows: set OPENAI_API_KEY=your-api-key
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Access the application at http://localhost:4200

## License

MIT
