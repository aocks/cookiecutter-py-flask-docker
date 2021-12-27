

.PHONY: clean help deployn

deploy:
	cp -r ../{{cookiecutter.project_slug}} flask/code/
	docker-compose build
	docker-compose up
