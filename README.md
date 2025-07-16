# Feature Flag Service

## Quickstart

1. Install dependencies:
   pip install -r requirements.txt

2. Run the server:
   uvicorn main:app --reload

3. Health check:
   curl http://localhost:8000/health

## Docker

Build and run:
   docker build -t feature-flag-service .
   docker run -p 8000:8000 feature-flag-service
