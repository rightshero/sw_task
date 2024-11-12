![alt text](https://rightshero.com/wp/wp-content/uploads/2024/04/RightsHero-Logo.png)


# Software Engineer Task Assessment

This role will be part of the Rightshero software development team.

As a software engineer you are a part of a small but very efficient and multi-tasking team. 

The team is tasked with handling all the software aspects of our service.

# The task
The task will be a **project** and **AWS CloudFormation** template:

## [1] The project:
A project contains one page have a 2 categories checkboxes

- [ ] Category A
- [ ] Category B

Unlimited subcategories of parent category (if it is hard to achieve the unlimited levels, you can set 3 levels hard-coded)
Should use Ajax.

### Example
- [ ] Category A
- [ ] Category B

If user select “Category B”
The system will create another 2 checkboxes with

- [ ] SUB Category B1
- [ ] SUB Category B2

Selecting Sub Category B2 will create another 2 checkboxes

- [ ] SUB SUB Category B2-1
- [ ] SUB SUB Category B2-2
 And so on


## [2] AWS CloudFormation
An AWS CloudFormation template YAML file for:
- Launch a t2.micro or t3.micro EC2 instance
- Create IAM role with admin privileges
- Attach the IAM role to the EC2 instance created earlier
- Deploy the project on the EC2 instance
- The instance should be accessable via SSH, HTTP and HTTPS protocols/ports


# Notes
- We would be scoring for the below aspects of the assignment:
- DB,Architecture /Code (preferred MVC pattern), Security, Git
- You could use a framework to create the project from scratch (Django).
- You should use MySQL or Postgresql Databases.
- Please use one table design in the database for all categories and subs.
- The code should contain comments with important information.
- README file for run the project locally.
- The **AWS CloudFormation** template file.


# Deliverables
- The project should be ready with docker compose (web service + DB).
- The **AWS CloudFormation** template YAML file.
- Once you're finished, submit a PR to this repo with your email in a commit message.
- The email should be the same as your email in the CV/Resume.

------------------------------------------------------------------------------------------------------------------------------

# Dynamic Category Tree (`rightshero/sw_task`)

## Project Overview

This project is designed to handle categories and subcategories with an AJAX-driven interface. The user can select from two primary categories, and based on the selection, additional subcategories appear dynamically. The system supports multiple levels of subcategories, with up to three levels hard-coded for simplicity.

here, provided instructions on how to run the project locally, deploy it on an EC2 instance via AWS CloudFormation, and configure necessary resources.

## Technologies Used

- **Backend**: Django Framework (MVT pattern)
- **Database**: MySQL or PostgreSQL (configured via Docker)
- **Frontend**: HTML, JS (AJAX for dynamic category loading)
- **Cloud**: AWS EC2, CloudFormation
- **Version Control**: Git

## Prerequisites

- Python 3.x
- Django (installed via `pip`)
- MySQL or PostgreSQL
- Docker (for running the project locally)
- AWS account (for deploying via CloudFormation)

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/hammoda711/dynamic-category-tree
cd <repository_directory>
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### Install Dependencies

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### Setup Database

1. Create a MySQL/PostgreSQL database on your local machine or configure it through Docker.
2. Update the `DATABASES` configuration in `settings.py` with the appropriate database details (host, user, password).

### Run the Project Locally

1. **Run Migrations**: Apply the database migrations to set up the schema.
  
  ```bash
  python manage.py migrate
  ```
  
2. **Create a Superuser**: If you need to access the Django admin panel, create a superuser.
  
  ```bash
  python manage.py createsuperuser
  ```
  
3. **Start the Server**: Run the development server.
  
  ```bash
  python manage.py runserver
  ```
  
4. Open `http://127.0.0.1:8000` in your browser to view the application.
  

### Accessing the Admin Panel

You can access the Django Admin panel at:

```bash
http://127.0.0.1:8000/admin
```

Login with the superuser credentials you created earlier.

## AWS CloudFormation Template

The CloudFormation template `cloudformation-template.yaml` will:

- Launch an EC2 instance (t2.micro or t3.micro)
- Create an IAM role with admin privileges
- Attach the IAM role to the EC2 instance
- Allow SSH, HTTP, and HTTPS access to the instance

### Running the Project on AWS

1. Deploy the CloudFormation template in AWS via the AWS Management Console or CLI.
2. After the EC2 instance is created, SSH into the instance and pull the latest code from your repository.
3. Set up the environment, install dependencies, and start the Django project.

## Docker Setup

The project includes a `docker-compose.yml` file to run the application and database in Docker containers.

1. Build the containers:
  
  ```bash
  docker-compose build
  ```
  
2. Start the services:
  
  ```bash
  docker-compose up
  ```

3. If you want to Runserver via Docker 

  ```bash
   docker-compose exec web python manage.py runserver 0.0.0.0:8001
  ```

## Security Considerations

- Ensure that the EC2 instance and the IAM role have the minimum necessary permissions.
- Secure sensitive data such as database credentials using environment variables or AWS Secrets Manager.
- Use HTTPS for secure communication.