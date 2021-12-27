FROM ubuntu:20.04

RUN apt update && apt install -y python3 python3-venv git

# upgrade pip

# permissions and nonroot user for tightened security
RUN adduser --disabled-password nonroot
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /home/app
USER nonroot

# copy all the files to the container
COPY --chown=nonroot:nonroot . .
RUN echo "files in WORKDIR:" && ls -al .
RUN mkdir -p ~/.ssh && \
    cp -n -r dot_ssh/* ~/.ssh/

ARG GIT_REPOS

# venv
ENV VIRTUAL_ENV=/home/app/venv

# python setup
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r requirements.txt

# Use the deploy_utils script to pull git repos
RUN python3 /home/app/deploy_utils.py pull-git-repos \
    --git-repos ${GIT_REPOS} --deploy-dir /home/app/code


# define the port number the container should expose
EXPOSE 5000

CMD ["python3", "-v", "/home/app/wsgi.py"]
