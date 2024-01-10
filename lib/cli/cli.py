# cli/cli.py
import click
from main import TodoApp

@click.group()
def cli():
    pass

@click.command()
def initdb():
    TodoApp.init_db()

@click.command()
def add_task():
    TodoApp.add_task()

@click.command()
def list_tasks():
    TodoApp.list_tasks()

cli.add_command(initdb)
cli.add_command(add_task)
cli.add_command(list_tasks)

if __name__ == '__main__':
    cli()
