from pathlib import Path

import click

from cli.add_source import add_source
# from cli.start import start
# from cli.stop import stop
# from cli.adduser import adduser
# from cli.removeuser import removeuser
from cli.logging import info


@click.group()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.pass_context
def main(ctx, verbose):
    """easyarchive is a command line tool for backing up files to a remote computer.  The remote
    computer should be running the easyarchive server.
    """

    home = Path.home()
    root = home.joinpath('.easyarchive')

    ctx.obj['HOME'] = home
    ctx.obj['ROOT'] = root

    init(ctx)

    if verbose:
        ctx.obj['VERBOSE'] = True
        info(ctx, "Entering VERBOSE mode.")


def init(ctx):
    pass
    # users_uploads = ctx.obj.get('USERS_UPLOADS')
    # users_credentials = ctx.obj.get('USERS_CREDENTIALS')
    #
    # if not users_uploads.exists():
    #     info(ctx, "Initializing users upload directory at: {0}".format(users_uploads))
    #     users_uploads.mkdir(parents=True, exist_ok=True)
    #
    # if not users_credentials.exists():
    #     info(ctx, "Initializing users credentials directory at: {0}".format(users_credentials))
    #     users_credentials.mkdir(parents=True, exist_ok=True)


main.add_command(add_source)
# main.add_command(stop)
# main.add_command(adduser)
# main.add_command(removeuser)
