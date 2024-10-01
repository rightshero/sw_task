COMPOSE_FILE = docker-compose.local.yml


upbuild:
	docker-compose -f $(COMPOSE_FILE) up --build

up:
	docker-compose -f $(COMPOSE_FILE) up

build:
	docker-compose -f $(COMPOSE_FILE) build

restart:
	docker-compose -f $(COMPOSE_FILE) restart

down:
	docker-compose -f $(COMPOSE_FILE) down

logs:
	docker-compose -f $(COMPOSE_FILE) logs $(filter-out $@,$(MAKECMDGOALS))

exec:
	docker-compose -f $(COMPOSE_FILE) exec $(filter-out $@,$(MAKECMDGOALS))
	
makemigrations:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

unittest:
	docker-compose -f $(COMPOSE_FILE) run --rm django python3 -m unittest discover -s $(filter-out $@,$(MAKECMDGOALS)) -p "test*.py"
flush:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py flush

createsuperuser:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py createsuperuser

startapp:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py startapp $(filter-out $@,$(MAKECMDGOALS))

collectstatic:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py collectstatic

command:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py $(filter-out $@,$(MAKECMDGOALS))

swagger:
	docker-compose -f $(COMPOSE_FILE) run --rm django python manage.py spectacular --file schema.yaml --validate --fail-on-warn
