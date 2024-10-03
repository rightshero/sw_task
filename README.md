# A Simple Software Task Written in django using Ajax for API calls

## local Installation

1. Clone the repository
2. Ensure you have docker and docker-compose installed if not install it from [here](https://docs.docker.com/get-docker/)
3. cd into the project directory.
4. Create a .env file in the root directory and add the following environment variables
```bash
    DEBUG=True
    SECRET_KEY=your_secret_key
    DJANGO_ALLOWED_HOSTS=localhost
    USE_DOCKER=yes
    IPYTHONDIR=/app/.ipython
    POSTGRES_DB=your_db_name
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_HOST=postgres   # this is the name of the postgres service in the docker-compose file
    POSTGRES_PORT=5432 # this is the default port for postgres you can change it if you want
```
### for make 
In the Makefile you need to change the COMPOSE_FILE var to __`docker-compose.local.yml`__

5. run 
### If you have make installed

```bash
    $ make upbuild
    $ make migrate
```

### If you dont have make installed
```bash
    $ docker compose -f docker-compose.local.yml up --build
    $ docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
```
6. Open your browser and navigate to [http://localhost:8000](http://localhost:8000)
7. Creating a superuser is necessary to access the admin panel. To create a superuser run
### For make
```bash
    $ make createsuperuser
```
### If you dont have make installed

```bash
    $ docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
```
8. To access the admin panel navigate to [http://localhost:8000/admin](http://localhost:8000/admin)
9. To create a categories using django commands run
### For make
```bash
    $ make command create_categories
```
### If you dont have make installed
```bash
    $ docker compose -f docker-compose.local.yml run --rm django python manage.py create_categories 
```


## production Installation


