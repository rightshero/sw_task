FROM python:3.9

# Create virtualenv outside the project folder
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Set working directory to /app
WORKDIR /app

# Install psycopg2 PostgreSQL dependency
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files
COPY . .

# Run migrations and start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
