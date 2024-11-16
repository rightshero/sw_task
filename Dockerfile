# Use the official Python image from the DockerHub
FROM python:3.10-slim

# Set the working directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .


# Install system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    openssl \
    && rm -rf /var/lib/apt/lists/*



# Copy Nginx configuration
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Create directory for SSL certificates
RUN mkdir -p /etc/nginx/ssl

# Generate self-signed SSL certificate for development
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/nginx.key \
    -out /etc/nginx/ssl/nginx.crt \
    -subj "/C=EG"

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt


COPY entrypoint.sh .
RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh


# Copy the content of the local src directory to the working directory
COPY . .

# Expose ports for http/https
EXPOSE 80 443

ENTRYPOINT ["sh", "./entrypoint.sh"]
