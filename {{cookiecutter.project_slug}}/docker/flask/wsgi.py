"""WSGI file to import {{cookiecutter.github_repos.split(',')[0]}} and run it.

This should basically only ver be run by a WSGI server.
"""

import os
from {{ cookiecutter.github_repos.split(',')[0].split('/')[-1] }}.apps import app_factory


if __name__ == "__main__":
    app = app_factory.create_app()
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"))
