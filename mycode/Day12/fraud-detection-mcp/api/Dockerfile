# Base Python image
FROM python:3.9-slim

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy model & API code
COPY ml_model/model.joblib .
COPY main.py .

# Run FastAPI on port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]FROM ubuntu:latest
LABEL authors="murali"

ENTRYPOINT ["top", "-b"]