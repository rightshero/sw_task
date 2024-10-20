

# 🧑🏽‍💻 Technologies Used
1. **Poetry** – as the package manager and virtual environment
2. **Django** – Python framework
3. **Docker & Docker Compose** – for containerization 

# ⚡️ Quick Start

## 0. Generate a Secret Key
To generate a secret key for your app, run the following command (requires Python):
```bash
python -c "import secrets; print(secrets.token_urlsafe(50).replace('-', '').replace('_', ''))"
```
Copy the generated key and add it to your `.env` file.

## 1. Create `.env` File
Inside the `SW_TASK` folder (e.g., `SW_TASK/.env`), create an `.env` file with the following content:

```bash
DEBUG=True
SECRET_KEY='your_secret_key'
DATABASE_URL="postgresql://DB_USER:PASSWORD@HOST:PORT/NAME"  # You don't need to change this, but it's better to customize for future needs.
NAME="category_db"  # Do not change unless modified in `database.env`.
DB_USER="your_db_username"  # Must match POSTGRES_USER in `database.env`.
PASSWORD="your_password"  # Must match POSTGRES_PASSWORD in `database.env`.
HOST="production_db"  # Use `localhost` if running the app without Docker. You must run the `production_db` service.
PORT="5432"  # Use port `5433` if running locally without Docker, but the `production_db` service must be running.
```

## 2. Create `database.env` File
Inside the `SW_TASK` folder (e.g., `SW_TASK/database.env`), create a `database.env` file with the following content:

```bash
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=category_db  # If you change this, also change it in the `.env` file.
```

## 3. Create `database_management.env` File
Inside the `SW_TASK` folder (e.g., `SW_TASK/database_management.env`), create a `database_management.env` file with the following content:

```bash
PGADMIN_DEFAULT_EMAIL="rightshere@gmail.com"  # Change this if you want to manage the database.
PGADMIN_DEFAULT_PASSWORD="1SG"  # Update the password if desired.
```

## 4. Ensure Docker and Docker Compose are Installed
Make sure that both Docker and Docker Compose are installed and Docker is running. Ensure that ports `8888`, `5433`, `5432`, and `8000` are available for the services.

## 5. Run the Application
Run the following command to start the app:
```bash
docker-compose up
```

Access the app at `localhost:8000`.

---

# Running Without Docker

## 1. Create `.env` File
Follow the same steps as in the Docker section to create the `.env` file.

## 2. Create `database.env` File
Create the `database.env` file with the same content as described earlier.

## 3. Create `database_management.env` File
Follow the steps above to create the `database_management.env` file.

## 4. Adjust Docker Compose
Either remove the `web` service from the `docker-compose.yml` file  or stop the web service and  run it 
```bash
docker-compose up
```


## 5. Install Dependencies and Run Locally
1. Navigate to the `SW_Task` folder.
2. Install Python.
3. Install `poetry==1.8.3` by running:
   ```bash
   pip install poetry==1.8.3
   ```
4. Install project dependencies:
   ```bash
   poetry install
   ```
5. Activate the virtual environment:
   ```bash
   poetry shell
   ```
6. Run database migrations:
   ```bash
   python categories_project/manage.py migrate
   ```
7. Seed the database with categories:
   ```bash
   python categories_project/manage.py init_categories
   ```
8. Start the Django development server:
   ```bash
   python categories_project/manage.py runserver
   ```

---

# [2] AWS CloudFormation

An AWS CloudFormation template YAML file is included. It:
- Creates environment files with some default values.
- Runs `docker-compose up`.
- Opens a custom TCP port (8000) for the development phase.

> **Note:** Running both the database and web services on the same instance is not recommended for production environments. 

---

# Note: check testing video