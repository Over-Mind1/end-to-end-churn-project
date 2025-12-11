# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing pyc files to disc and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (optional but recommended for some ML libraries)
# RUN apt-get update && apt-get install -y --no-install-recommends gcc libgomp1 && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the application
# Note: "main:app" assumes your file is named main.py and the FastAPI instance is named 'app'
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]