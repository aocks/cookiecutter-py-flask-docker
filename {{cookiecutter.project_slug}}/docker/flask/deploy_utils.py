"""Utilities to help deploy apps.
"""

import os
import subprocess
import logging

import click


@click.group()
def cli():
    "Command line interface for deployment tools."


@cli.command()
@click.option('--git-repos', envvar='GIT_REPOS', help=(
    'Comma separated list of repos to pull (e.g., emin63/ox_secrets,ab/cd).\n'
    'Will use GIT_REPOS env var as default.'))
@click.option('--deploy-dir', help=(
    'Parent dirctory for where to deploy git repos we pull.'))
@click.option('--loglevel', type=click.Choice([
    'DEBUG', 'INFO', 'WARNING', 'CRITICAL', 'ERROR']), default='INFO',
              help='log level to use')
def pull_git_repos(git_repos, deploy_dir, loglevel):
    """Pull necessary git repos.
    """

    logging.getLogger('').setLevel(getattr(logging, loglevel))
    if not git_repos:
        raise ValueError('No git repos provided.')
    if not deploy_dir:
        raise ValueError('Must provide --deploy-dir')
    for full_name in git_repos.split(','):
        shell_env = os.environ.copy()
        full_name = full_name.strip()
        repo = full_name.split('/')[-1]
        dk_file = f'{os.environ["HOME"]}/.ssh/dk_{repo}_id_rsa'
        if ':' not in full_name:
            if os.path.exists(dk_file):
                full_name = f'git@github.com:{full_name}'
                shell_env['GIT_SSH_COMMAND'] = (
                    f'ssh -vvv -i {dk_file} -o IdentitiesOnly=yes')
            else:
                logging.warning('No deploy key at %s; using https',
                                dk_file)
                full_name = f'https://github.com/{full_name}'

        my_dir = os.path.join(deploy_dir, repo)
        if not os.path.exists(my_dir):
            cmd = ['git', 'clone', full_name]
            logging.info('Clone via: %s', cmd)
            subprocess.check_call(cmd, cwd=deploy_dir,
                                  env=shell_env)

        cmd = ['git', 'pull']
        logging.info('Pulling via: %s', cmd)
        subprocess.check_call(cmd, cwd=my_dir, env=shell_env)

        req_file = os.path.join(my_dir, 'requirements.txt')
        if os.path.exists(req_file):
            cmd = ['pip', 'install', '-r', req_file]
            logging.info('Installing requirements: %s', cmd)
            subprocess.check_call(cmd, cwd=my_dir)


if __name__ == '__main__':
    cli()
