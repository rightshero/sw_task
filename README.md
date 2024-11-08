# Django Category Management Project

This project is a Django application that allows users to manage categories and subcategories dynamically. It includes a single page with checkboxes for categories and subcategories, with AJAX used to load subcategories based on user selections. The project is ready for deployment with Docker and AWS CloudFormation.

## Features
- Dynamic category and subcategory management with unlimited nesting (using AJAX).
- AWS CloudFormation template to set up an EC2 instance with IAM role and deploy the project.
- Docker setup with `docker-compose` for easy development and deployment.
- PostgreSQL database.
- Static file management using WhiteNoise for production.

## Technologies Used
- **Django**: Web framework.
- **AJAX**: For dynamic loading of subcategories.
- **PostgreSQL**: Database.
- **Docker**: Containerization.
- **AWS CloudFormation**: Infrastructure as code to launch and configure AWS resources.

---

## Project Structure

```plaintext
my_django_project/
├── app/                       # Main Django app
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files
│   ├── templates/             # HTML templates
│   ├── admin.py               # Admin customization
│   ├── models.py              # Database models
│   ├── views.py               # Application views
│   └── urls.py                # Application URLs
├── my_django_project/
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project URLs
│   ├── wsgi.py                # WSGI entry point for deployment
├── docker-compose.yml         # Docker Compose configuration
├── Dockerfile                 # Dockerfile for Django app
├── requirements.txt           # Python dependencies
├── cloudformation-template.yml # AWS CloudFormation template
└── README.md                  # Project documentation


Getting Started
Prerequisites
Docker & Docker Compose
AWS account (for CloudFormation deployment)
Python 3.8+
pip (Python package manager)




Notes::::::
I've attached my solution for the task, but this code reflects two days of work rather than a full week, as I had to return to my military service due to my leave has ended. I tried to write organized code, but I can’t claim this is a perfect or complete solution to the task. I'm ready for the technical interview.
Note: My military service will end in just two weeks.