# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system deps (for Earth Engine + shap)
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default start command for FastAPI web service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
