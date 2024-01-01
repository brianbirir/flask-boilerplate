PIPENV := pipenv run
DOCKER_RUN := docker-compose -f ../docker-compose.yml run --rm

db-migrate:
	$(PIPENV) flask db migrate
.PHONY: migrate

db-upgrade:
	$(PIPENV) flask db upgrade
.PHONY: migrations

server:
	gunicorn --reload --bind 0.0.0.0:8000 --timeout 600 --workers 1 "wsgi:create_app()"
.PHONY: server

run-server: \
    db-upgrade \
	server
.PHONY: run-server

start-services:
	docker-compose -f ../docker-compose.yml up
.PHONY: start-services

start-services-detached:
	docker-compose -f ../docker-compose.yml up -d
.PHONY: start-services

# should be run when docker services are running in detached mode
restart-services:
	docker-compose restart
.PHONY: stop-services

# should be run when docker services are running in detached mode
stop-services:
	docker-compose down
.PHONY: stop-services

# database initialization and migrations via docker compose run command
docker-initialize-db:
	$(DOCKER_RUN) flask_web_service $(PIPENV) flask db init
.PHONY: migrations

docker-run-migrate:
	$(DOCKER_RUN) flask_web_service $(PIPENV) flask db migrate
.PHONY: migrate

docker-run-migrations:
	$(DOCKER_RUN) flask_web_service $(PIPENV) flask db upgrade
.PHONY: migrations
