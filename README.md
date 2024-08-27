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


## Building, Running, and Testing the Project

This section provides a comprehensive guide to building, running, and testing the Django application using Docker. The project includes Docker configurations for local development, as well as instructions for running tests.

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Docker
- Docker Compose

### Setting Up the Environment

1. **Create a `.env` File:**

   Create a `.env` file inside the `.envs` directory with the following content:

   ```bash
   DEBUG=True
   ADMIN_URL=admin
   DATABASE_URL='postgresql://postgres:postgres@postgres_development:5432/rightsHero'
   REDIS_URL='redis://redis_development:6379/0'
   CELERY_FLOWER_USER=octo
   CELERY_FLOWER_PASSWORD=octo
   TYPE_STORAGE=local
   ```
  
2. **Build the Docker Containers:**
   
   Run the following command to build the Docker containers:

   ```bash
   docker-compose -f docker-compose.dev.yml up --build -d
   ```
   
3. **Run the Migrations:**
   
   Run the following command to apply the migrations:

   ```bash
   docker-compose -f docker-compose.dev.yml exec django python manage.py migrate
   ```
   or go inside the container and run the command
   ```bash
   just migrate
    ```
   
4. **Create a Superuser:**
    
    Run the following command to create a superuser:
    
     ```bash
     docker-compose -f docker-compose.dev.yml exec django python manage.py createsuperuser
     ```
     or go inside the container and run the command
     ```bash 
      just create-admin
     ```

5. **Access the Project:**
   
   Access the project by visiting `http://127.0.0.1:8080/en` in your web browser.
