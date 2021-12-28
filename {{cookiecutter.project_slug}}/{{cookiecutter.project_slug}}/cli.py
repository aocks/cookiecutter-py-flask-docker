"""Console script for {{cookiecutter.project_slug}}."""


import logging
import click
from flask.cli import FlaskGroup

from {{cookiecutter.project_slug}}.apps import app_factory


@click.group()
def cli():
    "Command line interface to manage {{cookiecutter.project_slug}}."


@cli.group(cls=FlaskGroup, add_default_commands=False)
@click.option('--loglevel', default='INFO', type=click.Choice(
    ['DEBUG', 'INFO', 'WARNING', 'CRITICAL', 'ERROR', 'FATAL']), help=(
        'Python logLevel'))
def fcli(loglevel):
    "Custom flask related commands"

    loglevel = getattr(logging, loglevel)
    app_factory.raw_set_startup_options(loglevel)


@fcli.command('serve')
@click.option('--host', '-h', default='0.0.0.0', help=(
    'Hosts to listen for on server; use 0.0.0.0 to listen for all'))
@click.option('--port', '-p', help='Port to use for server.',
              default=5555, type=int)
@click.option('--debug', '-d', help='Whether to run in debug mode.',
              default=0, type=int)
def serve(host, port, debug, my_app=None):
    'Run default server with default args.'

    my_app = my_app or app_factory.create_app()
    my_app.run(host=host, port=port, debug=debug)


def main():
    """Run the main command line.
    """
    return cli()


if __name__ == "__main__":
    main()
