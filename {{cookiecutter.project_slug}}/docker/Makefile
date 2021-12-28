

SHELL = /bin/bash

export NGINX_HTTP_PORT
export NGINX_SSL_PORT

.PHONY: clean help deployn

deploy:
	mkdir -p flask/code
	cp -r ../{{cookiecutter.project_slug}} flask/code/{{cookiecutter.project_slug}}
	docker-compose build
	docker-compose up

local_deploy:
	NGINX_HTTP_PORT=9080 NGINX_SSL_PORT=9443 ${MAKE} deploy

down:
	docker-compose down
