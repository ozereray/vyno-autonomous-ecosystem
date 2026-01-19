FROM python:3.8-slim
RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "03-The-Orchestrator/orchestrator.py"]