# Use a lightweight Python image
FROM python:slim

# Set environment variables to prevent Python from writing .pyc files & ensure Python output is not buffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies required by LightGBM and build tools for compiling packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY . .

# Upgrade pip first to avoid issues
RUN pip install --upgrade pip

# Install the package in editable mode and upgrade numpy (numpy might get built from source)
RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir --upgrade numpy

# Train the model before running the application
RUN python pipeline/training_pipeline.py

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "application.py"]
