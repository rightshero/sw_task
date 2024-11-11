# Use the official Python image from Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . /app/

# Expose port 8000 to be accessible on the host machine
EXPOSE 8000

# Set environment variables (optional)
# ENV DB_NAME=tree_db
# ENV DB_USER=tree_user
# ENV DB_PASSWORD=1234
# ENV DB_HOST=db
# ENV DB_PORT=5432

# Run migrations and start the Django application
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]