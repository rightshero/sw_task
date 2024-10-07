# Dockerfile
FROM python:3.9

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the server
CMD ["./wait-for-it.sh", "db:3306", "--", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
