"""WSGI file to import {{cookiecutter.project_slug}} and run it.

This should basically only be run by a WSGI server.
"""

import os
import sys
import logging
sys.path.append('/home/app/code')

from {{ cookiecutter.project_slug }}.apps import app_factory


if __name__ == "__main__":
    app = app_factory.create_app()
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"))
else:
    logging.warning('wsgi import as non-main but still creating app')
    app = app_factory.create_app()
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"))
