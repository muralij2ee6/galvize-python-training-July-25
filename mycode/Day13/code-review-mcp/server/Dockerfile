# ./server/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies (if needed for Ollama or other packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port your server runs on
EXPOSE 8000

# Command to run your server
CMD ["python", "main.py"]  # or whatever your server entrypoint is