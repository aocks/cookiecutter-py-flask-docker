

.PHONY: deploy local_deploy docker_down clean exec_nginx build
SHELL = /bin/bash

ifndef PROJECT
PROJECT={{cookiecutter.project_slug}}
endif


# Set default values for NGINX_HTTP_PORT and NGINX_SSL_PORT as used in
# the docker-compose file. You can override these mannually or by using
#      make local_deploy
# to use ports for testing as opposed to the canonical http/https ports

ifdef NGINX_HTTP_PORT
export NGINX_HTTP_PORT
else
export NGINX_HTTP_PORT := 80
endif

ifdef NGINX_SSL_PORT
export NGINX_SSL_PORT
else
export NGINX_SSL_PORT := 443
endif

ifdef FLASK_HTTP_PORT
export FLASK_HTTP_PORT
else
export FLASK_HTTP_PORT := 8000
endif


ifdef DOCKER_UP_FLAGS
export DOCKER_UP_FLAGS
else
export DOCKER_UP_FLAGS := -d
endif

ALL_DEPEND = flask/requirements.txt

flask/requirements.txt: ../requirements.txt
	cp ../requirements.txt flask/.

build: ${ALL_DEPEND}
	docker-compose build

nginx_volumes:
	docker inspect -f '{{ .Mounts }}' docker_nginxproxy_1

deploy: ${ALL_DEPEND}
	echo "Removing flask/code so we can copy over latest version"
	rm -r flask/code
	mkdir -p flask/code
	cp -r ../${PROJECT} flask/code/${PROJECT}
	${MAKE} build
	docker-compose up ${DOCKER_UP_FLAGS}

local_deploy: ${ALL_DEPEND}
	@echo "Making local deployment."
	NGINX_HTTP_PORT=9080 NGINX_SSL_PORT=9443 ${MAKE} deploy
	@echo " "
	@echo "IMPORTANT: point your browser to"
	@echo "   http://localhost:${FLASK_HTTP_PORT}"
	@echo "IMPORTANT: nginx will not be useful in a local deploy"
	@echo "Do 'make help_local_deploy' for more details."
	@echo " "

help_local_deploy:  ## Help on the local_deploy target
	@echo "The local_deploy target is for testing a local deployment."
	@echo "This is not great since nginx will probably not do what"
	@echo "you want in a local deployment and so all you can realy"
	@echo "do is using http (not https) to connect to the"
	@echo "flask container via something like"
	@echo "   http://localhost:${FLASK_HTTP_PORT}"
	@echo "and not use nginx or https."
	@echo " "
	@echo "If you want to test https and do it locally with oauth,"
	@echo "then use the serve_https makefile target in top-level."


docker_down:
	docker-compose down

exec_nginx:
	docker exec -it docker_nginxproxy_1 /bin/bash
