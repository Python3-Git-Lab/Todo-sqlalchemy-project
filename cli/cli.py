import click
from todo.cli_commands import initdb, add_task, list_tasks, dsa_example

@click.group()
def cli():
    pass

cli.add_command(initdb)
cli.add_command(add_task)
cli.add_command(list_tasks)
cli.add_command(dsa_example)

# Add more commands as needed

if __name__ == '__main__':
    cli()
