# Use a slim Python image (lightweight and fast)
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (optimizes Docker caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Tell Docker which port the app will use
EXPOSE 8000

# Command to run when the container starts
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]