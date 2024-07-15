# To-Do List Application

## Description
This To-Do List application is a simple yet powerful tool for managing your tasks. It allows you to add, edit, and delete tasks, set deadlines, and track your tasks in real-time. The application features a colorful and creative design with an intuitive user interface.

## Features
- Add new tasks with details and deadlines
- Edit existing tasks
- Delete tasks
- Real-time deadline tracking
- Choose between date-only or date-and-time deadlines
- Visual indicator for overdue tasks
- User-friendly GUI with a creative design

## Requirements
- Python 3.x
- Tkinter (usually included with Python)
- SQLite3 (usually included with Python)

## Installation
1. Clone the repository:
    ```bash
    git clone ---
    ```
2. Navigate to the project directory:
    ```bash
    cd To-Do-List
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

## Usage
1. Run the main application script:
    ```bash
    python main.py
    ```
2. The application window will open. Use the provided fields and buttons to manage your tasks.

## GUI Components
- **Task Name**: Enter the name of your task.
- **Task Detail**: Provide additional details for your task.
- **Deadline**: Set the deadline for your task. You can choose between a date-only or a date-and-time format.
- **Add Task**: Click to add a new task or save changes to an existing task.
- **Edit Task**: Select a task from the list, modify its details, and save changes.
- **Delete Task**: Select a task from the list and delete it.
- **Task List**: Displays all tasks with their details and status.

## Database
Tasks are stored in a SQLite database (`tasks.db`). The database schema includes:
- `id`: INTEGER PRIMARY KEY
- `task`: TEXT
- `detail`: TEXT
- `deadline`: TEXT
- `status`: TEXT

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



