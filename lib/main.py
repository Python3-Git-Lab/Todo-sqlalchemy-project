from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import click


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    user = relationship('User')
    category = relationship('Category')

DATABASE_URL = "sqlite:///todo.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def add_task():
    print("\nAdd task")
    title = input('Enter task title: ')
    description = input('Enter task description: ')
    category_id = int(input('Enter category ID: '))

    new_task = Task(title=title, description=description, category_id=category_id)
    SessionLocal.add(new_task)
    SessionLocal.commit()
    click.echo(f"Task '{title}' added successfully.")

def display_categories():
    print("\nCategories in the system:")
    categories = SessionLocal.query(Category.name).all()
    print(categories)

def list_tasks():
    print("\nList of tasks:")
    tasks = SessionLocal.query(Task).all()
    for task in tasks:
        print(f"Title: {task.title}, Description: {task.description}, Category: {task.category.name}")

def menu_options():
    print("\nSelect option: ")
    print("1. Add Task")
    print("2. Display Categories")
    print("3. List Tasks")
    print("4. Quit\n")
    choice = int(input("Please enter your option: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        display_categories()
    elif choice == 3:
        list_tasks()
    elif choice == 4:
        exit()
    else:
        print("Invalid option")

if __name__ == "__main__":
    print("\nWelcome to the To-Do List App\n--------------------------------")
    print("\nLet's get organized!")
    while True:
        menu_options()
