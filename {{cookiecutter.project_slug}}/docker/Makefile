

SHELL = /bin/bash

.EXPORT_ALL_VARIABLES
.PHONY: clean help deployn

deploy:
	cp -r ../{{cookiecutter.project_slug}} flask/code/
	docker-compose build
	docker-compose up

local_deploy:
	LOCAL_HTTP_PORT=9080 LOCAL_SSL_PORT=9443 ${MAKE} deploy

down:
	docker-compose down
