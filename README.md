![alt text](https://rightshero.com/wp/wp-content/uploads/2024/04/RightsHero-Logo.png)


# Software Engineer Task Assessment

This application allows users to select categories and subcategories in a hierarchical structure. It uses Django for the backend API, Django REST Framework for building the API, and a simple HTML/JavaScript frontend for user interaction.

## Features

*   Displays categories in a checkbox format.
*   Dynamically loads subcategories when a category is selected.
*   Automatically creates two new subcategories with predefined names when a category is selected.
*   Handles unlimited levels of subcategories (or up to a limit defined in the API).
*   Uses AJAX for seamless category loading and creation.

## Requirements

*   Python 3.12
*   Poetry
*   Docker
*   Docker Compose

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/sw_task.git](https://github.com/your-username/sw_task.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd sw_task
    ```
3.  Install dependencies using Poetry:
    ```bash
    poetry install
    ```
4.  Create and apply database migrations:
    ```bash
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate
    ```
5.  Create a superuser for the admin interface (optional):
    ```bash
    poetry run python manage.py createsuperuser
    ```

## Running the Application

1.  Build and run the Docker containers:
    ```bash
    docker-compose up -d
    ```
2.  Access the application in your browser:
    ```
    http://0.0.0.0:8000/
    ```

## API Documentation

The API endpoints for managing categories are available at:

*   **List all categories:** `/categories/`
*   **Create a new category:** `/categories/` (POST request)
*   **Get a specific category:** `/categories/{id}/`
*   **Update a category:** `/categories/{id}/` (PUT or PATCH request)
*   **Delete a category:** `/categories/{id}/` (DELETE request)

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
