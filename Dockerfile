# Base image for Python 3.11
FROM python:3.11-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory inside the container
WORKDIR /app
# Install system dependencies for MySQL and Python development
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    musl-dev \
    pkg-config \         
    && apt-get clean
# Copy requirements file
COPY requirements.txt /app/
# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt
# Copy project files to the container
COPY . /app/
# Run migrations and start Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




