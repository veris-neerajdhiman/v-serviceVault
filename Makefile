
.PHONY: runserver
runserver:
	python manage.py runserver 0.0.0.0:8014

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migration:
	python manage.py migrate

.PHONY: db_shell
db_shell:
	python manage.py dbshell

.PHONY: shell
shell:
	python manage.py shell_plus

.PHONY: superuser
superuser:
	python manage.py createsuperuser

# ---------------------------------------------------------------------------------------------------

# Makefile commands for docker


# -----------------------------------------------------------------------------------------------------

# Docker commands

.PHONY: build
build:
	docker build -t inforian/vault-service:${version} -f config/docker/Dockerfile .

.PHONY: image
image:
	docker images | grep vault-service

.PHONY: tag
tag:
	docker tag ${id} ${image}

.PHONY: push
push:
	docker push ${tag}

.PHONY: run
run:
	docker run -it --publish=8001:8000 $(id)