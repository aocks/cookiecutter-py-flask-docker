

SHELL = /bin/bash

export NGINX_HTTP_PORT=80
export NGINX_SSL_PORT=443

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
