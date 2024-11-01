# Rightshero Project

This project is a simple Django-based web application deployed using Docker and AWS. The application allows users to interact with hierarchical categories using AJAX. The infrastructure for the deployment is automated using AWS CloudFormation.

## Features

- Django backend for managing categories and subcategories dynamically.
- AJAX integration for creating unlimited subcategories interactively on the frontend.
- PostgreSQL database for storing categories and subcategories.
- Docker for containerizing the application for easy setup.
- CloudFormation template to automate the deployment on AWS EC2 instance.

## Getting Started

These instructions will help you get the project up and running on your local machine.

### Prerequisites

- Python 3.11
- Django 4.2 (LTS)
- Docker & Docker Compose
- AWS CLI (optional, if deploying on AWS)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/usamaalzomor/sw_task
   cd sw_task
   ```

2. **Set up Python environment**:

   - Create a virtual environment:
     ```bash
     virtualenv --python=/path/to/python3.11 venv  # this creates virtualenv with python3.11 (recommended version of python)
     source venv/bin/activate  
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set up environment variables**:

   - The project includes a `.env` file that is already set up for use with Docker Compose. The environment variables inside it are suitable for running the project using Docker. If you need to run it locally without Docker, modify the `.env` file or create a new `.env.local` file with the appropriate values for your local environment.

   - **Note**: If you are running the project locally without Docker, you should modify the `DATABASE_URL` variable to point to your local PostgreSQL instance, for example:
     ```
     DATABASE_URL=postgres://postgres:yourpassword@localhost:5432/yourdatabase
     ```

### Running with Docker

1. **Build and run Docker containers**:

   ```bash
   docker-compose up --build
   ```

2. **Access the application**: The app will be accessible at [http://localhost:8000/categories/](http://localhost:8000/categories/).


### Running the Project Locally

1. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

2. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

3. **Access the application**: Open [http://127.0.0.1:8000/categories/](http://127.0.0.1:8000/categories/) in your browser.


### AWS Deployment

The project includes a CloudFormation YAML template for automated deployment to AWS EC2.

1. **Validate the CloudFormation Template**:

   ```bash
   cfn-lint cloudformation_template.yaml
   ```

2. **Deploy Using AWS CLI**:

   ```bash
   aws cloudformation create-stack --stack-name rightshero-stack --template-body file://cloudformation_template.yaml --capabilities CAPABILITY_NAMED_IAM
   ```

   > Note: Make sure to replace placeholder values for `KeyName` and `ImageId` in the `cloudformation_template.yaml`.


### Key Endpoints

- `/categories/` - Endpoint to view all top-level categories.
- `/load-subcategories/` - AJAX endpoint to dynamically load subcategories.
- `/admin/` - Admin panel to manage categories and view the created subcategories.

### Admin Panel Access

You can access the Django admin panel to manage and view all categories, including subcategories, at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Use the username `admin` and password `admin` to log in. These credentials are automatically created during Docker setup using the variables in the `.env` file (`DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD`).

## Notes

- The environment variables in the `.env` file are configured for Docker usage. If running the project locally without Docker, ensure to update the `.env` values accordingly, particularly the `DATABASE_URL`.
- The `.env` file also includes settings for automatic superuser creation when using Docker. If you need to change the admin user details, modify the `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, and `DJANGO_SUPERUSER_PASSWORD` variables.
- Placeholder values in the CloudFormation template (like `KeyName` and `AMI ID`) need to be updated with actual values before deployment.
- Make sure to replace the Django `SECRET_KEY` in production for security purposes.


## Authors

- Usama Alzomor
