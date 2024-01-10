# main.py
from database import init_db, SessionLocal
from models import Task, User, Category
from sqlalchemy.orm import joinedload

class TodoApp:
    @staticmethod
    def init_db():
        init_db()

    @staticmethod
    def add_task():
        print("\nAdd task")
        title = input('Enter task title: ')
        description = input('Enter task description: ')
        category_id = int(input('Enter category ID: '))

        # Fetch the user and category
        user_id = int(input('Enter user ID: '))  # Assuming you have a user management system
        user = SessionLocal.query(User).get(user_id)
        category = SessionLocal.query(Category).get(category_id)

        if user is None or category is None:
            print("Invalid user or category ID. Task not added.")
            return

        new_task = Task(title=title, description=description, user=user, category=category)
        SessionLocal.add(new_task)
        SessionLocal.commit()
        print(f"Task '{title}' added successfully.")

    @staticmethod
    def list_tasks():
        print("\nList of tasks:")
        tasks = SessionLocal.query(Task).options(joinedload(Task.user), joinedload(Task.category)).all()
        for task in tasks:
            print(f"Title: {task.title}, Description: {task.description}, User: {task.user.username}, Category: {task.category.name}")
