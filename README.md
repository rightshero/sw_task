# category_project
This project has been developed in Django.
It uses a MySQL database with a single table to manage all categories and subcategories.
The application is containerized using Docker Compose, making it easy to run locally and deploy to cloud environments.

Prerequisites
Python 3.8 or higher
Django 3.2 or higher
MySQL client for database management
Docker, Docker Compose, Docker Desktop installed on your local machine

Setup Instructions
1. Clone the Repository
git clone https://github.com/<user>/category_project.git


2. Build and Run the Containers
docker-compose up --build

3. Apply Migrations
python3 manage.py migrate --run-syncdb

4. Access the Application
	http://localhost:8000/admin.
