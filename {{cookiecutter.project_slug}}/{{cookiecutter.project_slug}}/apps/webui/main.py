"""Main implementation of top level web UI.
"""

from flask import Flask

from {{cookiecutter.project_slug}}.apps.webui import views


def create():
    """Create flask app for main web UI.

    This is intended to be called by app_factory.py.
    """
    app = Flask(__name__)
    app.add_url_rule('/', 'home', view_func=views.home)
    app.add_url_rule('/flask-health-check', 'flask_health_check',
                     view_func=views.flask_health_check)

    return app
