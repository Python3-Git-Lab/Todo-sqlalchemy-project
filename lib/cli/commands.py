import click
from todo.database import SessionLocal
from todo.models import Task

@click.group()
def cli():
    pass

@cli.command()
@click.option('--title', prompt='Task Title', help='Title of the task')
@click.option('--description', prompt='Task Description', help='Description of the task')
@click.option('--due-date', prompt='Due Date (YYYY-MM-DD)', help='Due date of the task')
def add_task(title, description, due_date):
    session = SessionLocal()
    task = Task(title=title, description=description, due_date=due_date)
    session.add(task)
    session.commit()
    print(f"Task {title} added successfully.")

@cli.command()
def list_tasks():
    session = SessionLocal()
    tasks = session.query(Task).all()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{'X' if task.completed else ' '}] {task.title} - {task.description}")

@cli.command()
@click.argument('task_id', type=int)
def complete_task(task_id):
    session = SessionLocal()
    task = session.query(Task).filter_by(id=task_id).first()

    if not task:
        print(f"Task with ID {task_id} not found.")
        return

    task.completed = True
    session.commit()
    print(f"Task {task.title} marked as completed.")

if __name__ == "__main__":
    cli()
