"""WSGI script to create flask app locally.

Also useful for flask command line usage since if you use the
manage.py script, it will want to see a wsgi.py file.
"""

from {{cookiecutter.project_slug}}.apps.app_factory import create_app


if __name__ == "__main__":
    APP = create_app()
    APP.run()
