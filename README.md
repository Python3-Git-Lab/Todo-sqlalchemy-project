# To-Do List CLI App
This is a simple command-line interface (CLI) application for managing tasks in a To-Do List. The application is built using Python and SQLAlchemy, adhering to best practices and providing a clean and efficient solution for organizing your tasks.

## Project Structure
The project is organized into the following directories:

`todo/`: Contains the application's models and database configuration.
`cli/`: Contains the CLI commands to interact with the To-Do List.
`tests/`: Includes unit tests for critical components.
`Pipfile` and `Pipfile.lock`: Define project dependencies using Pipenv.
`main.py`: Entry point to run the CLI application.

### Installation
1. Clone the repository:

`git clone https://github.com/Mariegacheri/To-Do-List-App-Project/tree/main`

2. Navigate to the project directory:
`cd To-Do-List-App-Project`

3. Install dependencies using Pipenv:
`pipenv install`

4. Activate the virtual environment:
`pipenv shell`

## Usage
### Adding a Task
- To add a new task to the To-Do List, use the following command:
`python main.py add_task`
- You will be prompted to enter the title, description, and due date of the task.

### Listing Tasks
- To view the list of tasks in the To-Do List, use the following command:
`python main.py list_tasks`
- This command will display all tasks, indicating whether they are completed or not.

### Completing a Task
- To mark a task as completed, use the following command:
`python main.py complete_task <task_id>`
- Replace <task_id> with the ID of the task you want to mark as completed.

### Prioritizing Tasks
- To prioritize tasks based on due date, use the following command:
`python main.py prioritize_tasks`
- This command will display the tasks in order of their due dates.

## Database Configuration
The application uses SQLAlchemy to manage tasks and their details. The database is stored in a SQLite file (todo.db). If you need to make changes to the database schema, consider using migrations.

## Testing
- To run unit tests, use the following command:
`python -m pytest`
- This will execute tests in the tests/ directory and ensure the correctness of the application.

## Contributing
Feel free to contribute to the project by opening issues or creating pull requests. Your feedback and suggestions are highly appreciated.

## License
This project is licensed under the MIT License.

## Author
1. David Muchoki
2. Mary njeri