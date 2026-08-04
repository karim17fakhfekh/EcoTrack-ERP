FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose Flask port
EXPOSE 8080

# Run with Gunicorn WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
