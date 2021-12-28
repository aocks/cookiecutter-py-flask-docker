"""Module to make the flask apps for {{cookiecutter.project_slug}}
"""

import socket
import logging


def raw_set_startup_options(loglevel=logging.INFO):
    """Do setup stuff that will apply to all flask apps and blueprints.
    """

    root_logger = logging.getLogger('')
    root_logger.warning('Setting loglevel to %s', loglevel)
    root_logger.setLevel(loglevel)

    # Every once in a blue moon we will get things frozen and hung
    # unless we make sure hung sockets timeout so set timeout.
    dtimeout = 1201
    logging.warning('Doing socket.setdefaulttimeout(%s)', dtimeout)
    socket.setdefaulttimeout(dtimeout)


def create_app(loglevel=logging.INFO):
    """Create main flask app for {{cookiecutter.project_slug}}.

    This is sometimes called explicitly and sometimes auto-loaded
    (e.g., by `flask` cli). If desired you could have this function
    decide which app(s) and which blueprint(s) to load.
    """
    raw_set_startup_options(loglevel=loglevel)

    # Do imports as late as possible so changes to various settings
    # can be seen by flask

    from {{cookiecutter.project_slug}}.apps.webui \
        import main  # pylint: disable=import-outside-toplevel

    my_app = main.create()

    return my_app
