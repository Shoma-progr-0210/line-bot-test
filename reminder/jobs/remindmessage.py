import click
from flask.cli import with_appcontext

@click.command('remind', help="remind message")
@with_appcontext
def remind_message():
    print("hello world!!!")