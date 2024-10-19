# RightsHero Software Engineer Task Assessment

This project is part of the RightsHero software engineer task assessment. It implements a recursive category selection page with dynamic checkboxes using Django for the backend and Vue.js for the frontend. Docker is used to manage the backend, database, and frontend environments.

## Project Overview

The task includes two main components:

1. **Recursive Category Selection**  
   A page with dynamic checkboxes for categories and subcategories. Each parent category can have an unlimited number of child categories. Categories are managed using a Django backend with PostgreSQL, and the frontend is built using Vue.js.

2. **AWS CloudFormation** (Not deployed)  
   A YAML file for launching an EC2 instance with IAM roles and deploying the project, which is not included due to the lack of a credit card for deployment.

## Technologies Used

- **Backend**: Django 4.2.16 with Django Rest Framework (DRF) and PostgreSQL.
- **Frontend**: Vue.js 3 with Ajax for dynamic category selection.
- **Docker**: Used to containerize the backend, frontend, and database.
- **Database**: PostgreSQL.

## Project Structure

├── rightshero/ │ ├── categories/ # Django app for category management │ ├── manage.py # Django project management script │ └── Dockerfile # Dockerfile for the Django backend ├── frontend/ │ ├── src/ # Vue.js components and frontend logic │ └── Dockerfile # Dockerfile for the Vue.js frontend ├── docker-compose.yml # Docker Compose configuration for backend, database, and frontend └── README.md # Project overview and setup instructions

## Prerequisites

Before starting, make sure you have the following installed:

- Docker
- Docker Compose
- Git

## Setup and Run Locally

docker-compose up --build
This will:

    Create and run Docker containers for the Django backend, Vue.js frontend, and PostgreSQL database.
    Run database migrations automatically and create 5 initial categories.

## Access the Project

    The backend will be available at: http://localhost:8000.
    The frontend will be available at: http://localhost:8080.
## Contact Information
radwa.kaml00@eng-st.cu.edu.eg