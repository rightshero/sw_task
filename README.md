# Dynamic Categories Project

This project is a Django web application that allows users to dynamically select categories and subcategories using AJAX. The project is Dockerized for easy setup and also includes an AWS CloudFormation template for deploying the app on AWS.

## Project Structure

- **Backend**: Django
- **Frontend**: HTML + AJAX
- **Database**: MySQL (via Docker)
- **Containerization**: Docker Compose
- **Deployment**: AWS CloudFormation

---

## Prerequisites

Ensure you have the following installed on your machine:

- [Docker]
- [Docker Compose]
- AWS CLI configured with administrative access if deploying on AWS.

---

## Running Locally with Docker Compose

Follow these steps to set up and run the project locally using Docker Compose:

1. **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Set up environment variables:**

    Create a `.env` file in the project root directory and set your environment variables:

    ```
    DATABASE_URL=mysql://root:rootpassword@db:3306/mydatabase
    MYSQL_DATABASE=mydatabase
    MYSQL_PASSWORD=rootpassword
    MYSQL_ROOT_PASSWORD=rootpassword
    ```

3. **Build and run the containers:**

    Use Docker Compose to build and start the application and database containers:

    ```bash
    docker-compose up --build
    ```

4. **Access the application:**

    Once the containers are running, you can access the web application at:

    ```
    http://localhost:8000/
    http://localhost:8000/categories/
    ```

5. **Running Django commands:**

    To run Django management commands (such as migrations), use the following command:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

---

## Database Setup

The project uses a MySQL database. The database will be created automatically when you run the project with Docker Compose. If you need to interact with the database container (e.g., to check the tables), use:

```bash
docker-compose exec db mysql -u root -p
```

## Sub Categories Creation

Creating Unlimited subcategories of parent category while checking the parent category.