"""WSGI file to import {{cookiecutter.github_repos.split(',')[0]}} and run it.

This should basically only be run by a WSGI server in the docker container.
"""

import os

# NOTE: You may want to add lines like
#   sys.path.append('/home/app/code/<REPO>')
# here for any additional repos you want the app to access.

from {{ cookiecutter.github_repos.split(',')[0].split('/')[-1] }}.apps.app_factory import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"))
