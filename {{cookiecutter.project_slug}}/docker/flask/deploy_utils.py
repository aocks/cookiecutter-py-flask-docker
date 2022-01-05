"""Utilities to help deploy apps.
"""

import base64
import os
import subprocess
import logging

import click


@click.group()
def cli():
    "Command line interface for deployment tools."


@cli.command()
@click.option('--inject', envvar='INJECT_VARS_TO_FILES', help=(
    'Comma separated name:value pairs to inject as files.\n'
    'A value of --inject VNAME_1:FNAME_1:VAL_1,VNAME_2:FNAME_2:VAL_2\n'
    'would result in base64 decoding VAL_1, saving it in file\n'
    'named FNAME_1 and then doing the same for the variable in \n'
    'VNAME_2 and so on.'))
@click.option('--splitlist', default=',', help=(
    'How to split the --inject option list (default ",").'))
@click.option('--splititem', default=':', help=(
    'How to split items in the --inject option list (default ":").'))
def extract_files(inject, splitlist, splititem):
    """Extract files and write them.
    """
    msg = []
    if not inject and not inject.strip():
        msg.append('No value provided for --inject')
    else:
        item_list = inject.split(splitlist)
        for item in item_list:
            var_name, orig_location, var_value = item.split(splititem)
            file_location = os.path.abspath(orig_location)
            decoded = base64.b64decode(var_value)
            with open(file_location, 'wb') as fdesc:
                fdesc.write(decoded)
        msg.append(f'Injected file to {file_location}')
    click.echo('\n'.join(msg))


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
