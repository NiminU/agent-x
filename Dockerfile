FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create templates directory if it doesn't exist
RUN mkdir -p templates

EXPOSE 4200

CMD ["python", "app.py"]