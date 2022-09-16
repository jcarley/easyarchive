import click

from .logging import info, error


@click.command()
@click.option('--source', '-s', default='', required=True, type=str,
              help="The absolute folder location that you want to add to the backups")
@click.pass_context
def add_source(ctx, source: str):
    if len(source) > 0:
        folder_location = source
    else:
        error(ctx, "Source folder is required")
        return

    info(ctx, "Adding a new source location: {0}".format(folder_location))
