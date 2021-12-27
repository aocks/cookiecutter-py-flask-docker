#!/bin/bash

# Script to prepare conf files and then start nginx

# Copy conf files from /app, put in env variables
# and then move into nginx location. Must do this
# as root in case /etc/nginx/... is volume mounted
# as root user.
cp /app/default.conf /tmp/default.conf
envsubst '$FLASK_SERVER_ADDR:$FLASK_SERVER_NAME' < /tmp/default.conf > /etc/nginx/conf.d/default.conf

nginx -g 'daemon off;'
