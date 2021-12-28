

.PHONY: deploy local_deploy down clean
SHELL = /bin/bash



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

ifdef DOCKER_UP_FLAGS
export DOCKER_UP_FLAGS
else
export DOCKER_UP_FLAGS := -d
endif

deploy:
	mkdir -p flask/code
	cp -r ../{{cookiecutter.project_slug}} flask/code/{{cookiecutter.project_slug}}
	docker-compose build
	docker-compose up ${DOCKER_UP_FLAGS}

local_deploy:
	NGINX_HTTP_PORT=9080 NGINX_SSL_PORT=9443 ${MAKE} deploy

down:
	docker-compose down
