# Rightshero Task

## Description

This project is a Django web application that dynamically manages categories and subcategories using Ajax. The application allows users to select categories, which dynamically generate subcategories based on their selection.

## Requirements

- Python 3.8 or later
- Django 5.1
- Docker 
- Docker Compose 

## Setup and Installation

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Shehab1106/rightshero.git
cd your-repo
2. Set Up a Virtual Environment
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt

4. Configure Database Settings
Update the DATABASES setting in Rightshero_Task/settings.py to match your local environment. For PostgreSQL:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rightshero',
        'USER': 'rightshero_user',
        'PASSWORD': '0000',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Apply Migrations
Run the database migrations:

bash
Copy code
python manage.py migrate

6. Create a Superuser
Create a superuser for the Django admin interface:

bash
Copy code
python manage.py createsuperuser

7. Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver 0.0.0.0:8000
The application will be available at http://localhost:8000/.

Accessing the Application

Frontend: Visit http://localhost:8000/myapp/ to access the main application.

Admin Interface: Visit http://localhost:8000/admin to access the Django admin interface. Log in with the superuser credentials you created.

Project Structure

Rightshero_Task/
Dockerfile
manage.py
requirements.txt
myapp/
views.py - Handles AJAX requests and renders pages
urls.py - URL routing for the application
models.py - Defines the Django models for categories and subcategories
requirements.txt - Lists Python package dependencies
templates/
categories.html - Template for rendering categories and subcategories
Rightshero_Task/
settings.py - Django settings
urls.py - Root URL routing
static/
css/
styles.css
js/
categories.js

Notes

Replace placeholders in the DATABASES setting with your actual database credentials.

Ensure that ALLOWED_HOSTS in Rightshero_Task/settings.py includes localhost or 127.0.0.1 for local development.
License

Author
Shehab Sherif - shehabsmostafa@yahoo.com
