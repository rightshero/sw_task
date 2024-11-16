## 1. The project
A project contains one page have a 2 categories checkboxes

- [ ] Category A
- [ ] Category B

Unlimited subcategories of parent category

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

The project uses [Django](https://www.djangoproject.com/) for the backend, [nginx](https://nginx.org/en/) as a reverse-proxy and [gunicorn](https://gunicorn.org/) as an http server.

## 2. Running The Project Locally

1. create a local .env file containing the following variables:

```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=db-name
DB_USER=db-username
DB_PASSWORD=db-password
DB_HOST=db-host
DB_PORT=db-port
DJANGO_SECRET=django-secret-key
```
2. Install Docker and docker-compose

Docker installed: https://docs.docker.com/get-docker/
Docker Compose installed: https://docs.docker.com/compose/install/   

3. Build and run the web-service locally

```bash
docker-compose up
```

## 3. Deployment on AWS

1. Install the aws-cli

```
pip install aws-cli
```


2. Create a `parameters.json` file in the project root directory with the following structure:

```json
[
    {
      "ParameterKey": "KeyName", 
      "ParameterValue": "your_ssh_key_name"
    },
    {
      "ParameterKey": "dbEngine",
      "ParameterValue": "django.db.backends.postgresql"
    },
    {
      "ParameterKey": "dbName",
      "ParameterValue": "your_database_name"
    },
    {
      "ParameterKey": "dbUser",
      "ParameterValue": "your_database_username"
    },
    {
        "ParameterKey": "dbPassword",
        "ParameterValue": "your_database_password"
    },
    {
        "ParameterKey": "dbHost",
        "ParameterValue": "your_database_host"
    },
    {
        "ParameterKey": "dbPort",
        "ParameterValue": "your_database_port"
    },
    {
      "ParameterKey": "djangoSecret",
      "ParameterValue": "your_django_secret_key"
    }
]

```


3. Deploy the project as a cloudformation stack

```bash

aws cloudformation create-stack \
  --stack-name rightshero-stack \
  --template-body file://cloudformation.yaml \
  --parameters file://parameters.json \
  --capabilities CAPABILITY_NAMED_IAM

```