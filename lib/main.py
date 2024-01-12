# main.py
from models import Task, User, Category, session
from sqlalchemy.orm import joinedload
class Todo:
    def add_user():
        print("\nAdd user\n")
        name= input("Enter username: ")

        new_user= User(username= name)
        session.add(new_user)
        session.commit()
        session.close()
        print("\nUser added successifully")

    def add_task():
        print("\nAdd task to your\n")
        title= input("Enter the title of the task: ")
        description= input("Enter task description: ")
        status= input("Task complete YES/NO: ")
        user_id= int(input("Enter staff_id undertaking the task: "))

        new_task = Task(title=title, description=description, status= status, user_id=user_id)
        session.add(new_task)
        session.commit()
        session.close()
        print("\n Task has been added successifully")

    def add_category():
        print("\nAdd Task Category\n")
        name= input("Enter Category name: ")
        task_id= int(input("Enter the task id: "))

        new_task= User(name= name, task_id=task_id)
        session.add(new_task)
        session.commit()
        session.close()
        print("\nTask added successifully")

    def remove_task():
        """Remove a task by its ID"""
        try:
            task_id = int(input("\nEnter the task ID you would like to delete: "))
            task = session.query(Task).filter(Task.id ==task_id).first()
            #raise exception if no such task exists in database
            session.delete(task)
            session.commit()
            session.close()
            print("Task deleted successifully")
        except:
            print("\nNo task found with that ID")

    def remove_category():
        """Remove a category by its ID"""
        try:
            cat_id = int(input("\nEnter the category ID you would like to delete: "))
            cat = session.query(Category).filter(Category.id==cat_id).first()
            session.delete(cat)
            session.commit()
            session.close()
            print("Category Deleted Successfully!\n")
        except:
            print("\nThat is not a valid category ID.")

    def view_tasks():
        try:
            task_list = session.query(Task).all()
            for t in task_list:
                print(f"\nID: {t.id} Description: {t.title} Status: {t.status}")
        except:
            print("\nThere are currently no tasks saved.\n")

if __name__ == '__main__':
    print("\nManage your task efficiently")
    print("---------------------------------------")
    while True:
        print("\nMenu")
        print('1. View all tasks')
        print('2. Add a new task')
        print('3. Remove a task')
        print('4. Add a new category')
        print('5. Delete a category')
        print('6. Quit')
        choice = int(input('\nChoose an option (1-6): '))
        if choice == 1:
            Todo.view_tasks()
        elif choice== 2:
            Todo.add_task()
        elif choice == 3:
            Todo.remove_task()
        elif choice== 4:
            Todo.add_category()
        elif choice== 5:
            Todo.remove_category()
        elif choice== 6:
            break
        else:
            print("\nInvalid Option\n")