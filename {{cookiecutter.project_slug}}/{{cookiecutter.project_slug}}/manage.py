"""Console script for {{cookiecutter.project_slug}}.

Run this as something like

  python3.py manage.py --help

"""

import logging
import os
import click
from flask.cli import FlaskGroup


from {{cookiecutter.project_slug}}.apps import app_factory


@click.group()
def cli():
    "Command line interface to manage {{cookiecutter.project_slug}}."
    pass


@cli.group(cls=FlaskGroup, add_default_commands=False)
@click.option('--loglevel', type=int, default=logging.INFO, help=(
    'Python logLevel. Use %i for DEBUG, %i for INFO, etc.' % (
        logging.DEBUG, logging.INFO)))
def fcli(loglevel):
    "Custom flask related commands"
    app_factory.raw_set_startup_options(loglevel)


@fcli.command('serve')
@click.option('--host', '-h', default='0.0.0.0', help=(
    'Hosts to listen for on server; use 0.0.0.0 to listen for all'))
@click.option('--port', '-p', help='Port to use for server.',
              default=5000, type=int)
@click.option('--use-ssl', '-u', help=(
    'Use SSL directly via "adhoc" context for testing.'),
              default=0, type=int)
@click.option('--debug', '-d', help='Whether to run in debug mode.',
              default=0, type=int)
def serve(host, port, debug, use_ssl=0, my_app=None):
    'Run default server with default args for {{cookiecutter.project_slug}}'

    my_app = my_app or app_factory.create_app()
    root = os.path.abspath(os.path.dirname(app_factory.__file__))
    app_factory.serve(
        app=my_app, cert='adhoc' if use_ssl else None, host=host,
        port=port, debug=debug, use_ssl=use_ssl)


@cli.command()
def info():
    'Show information about management CLI'
    msg = '''This command line interface is used to manage {{cookiecutter.project_slug}}

You can use this to execute general commands like this one as well as
flask related commands via the fcli group.  It is better to use this
than the default flask CLI.  For example, `flask run` will not accept
or setup SSL correctly.  '''
    click.echo(msg)


if __name__ == '__main__':
    sys.exit(cli())  # pragma: no cover

