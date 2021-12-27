"""WSGI script to create flask app.

Also useful for flask command line usage.
"""

from python_boilerplate.apps import app_factory


def create_app():
    """WSGI create_app method which calls create_app from app_factory.

    This is only provided since the flask cli looks for it by default.
    We just use it to call the app_factory.create_app.
    """
    app = app_factory.create_app()
    return app


if __name__ == "__main__":
    APP = create_app()
    APP.run()
