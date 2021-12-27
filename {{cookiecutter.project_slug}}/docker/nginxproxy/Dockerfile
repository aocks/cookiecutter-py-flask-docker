FROM nginx:1.21.4

RUN apt update && apt install -y python3-certbot-nginx sudo

# Add nginx conf files to container
COPY default.conf /app/default.conf
COPY start.sh /app/start.sh
RUN chmod ugo+rx /app/*

# # Uncomment to keep the nginx logs inside the container - Leave commented for logging to stdout and stderr
# RUN mkdir -p /var/log/nginx
# RUN unlink /var/log/nginx/access.log \
#     && unlink /var/log/nginx/error.log \
#     && touch /var/log/nginx/access.log \
#     && touch /var/log/nginx/error.log \
#     && chown nginx /var/log/nginx/*log \
#     && chmod 644 /var/log/nginx/*log

CMD ["/app/start.sh"]
