# Task Manager CLI

A simple command-line interface (CLI) application to manage tasks, built using Python. This application allows users to add, update, delete, and list tasks while storing the data in a JSON file.

## Features

- **Add Tasks**: Add a new task with a description.
- **Update Tasks**: Modify the description of an existing task.
- **Delete Tasks**: Remove a task by its unique ID.
- **List Tasks**:
  - View all tasks.
  - Filter tasks by status (e.g., `todo`, `in-progress`, `done`).
- **Mark Tasks**: Update the status of a task to `todo`, `in-progress`, or `done`.

## Task Properties

Each task includes:
- `id`: A unique identifier.
- `description`: The task's details.
- `status`: Current status (`todo`, `in-progress`, `done`).
- `createdAt`: Timestamp when the task was created.
- `updatedAt`: Timestamp when the task was last updated.

## Requirements

- Python 3.6 or later

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-manager-cli.git
   cd task-manager-cli
2. Ensure python is installed
    ```bash
    python --version
3. Run the program using python
   ```bash
   python cli.py <command> [arguments]
   
## Command Reference Table

| Command      | Arguments                            | Description                                                                 | Example                                |
|--------------|--------------------------------------|-----------------------------------------------------------------------------|----------------------------------------|
| `add`        | `<description>`                     | Adds a new task with the given description.                                | `python cli.py add "Buy groceries"`   |
| `update`     | `<id> <new_description>`            | Updates the description of a task by its ID.                               | `python cli.py update 1 "New desc"`   |
| `delete`     | `<id>`                              | Deletes the task with the specified ID.                                    | `python cli.py delete 1`              |
| `mark`       | `<id> <status>`                     | Updates the status of a task to `todo`, `in-progress`, or `done`.           | `python cli.py mark 1 done`           |
| `list`       |                                      | Lists all tasks.                                                           | `python cli.py list`                  |
| `list`       | `<status>`                          | Lists tasks filtered by the specified status (`todo`, `in-progress`, `done`).| `python cli.py list done`             |

   
