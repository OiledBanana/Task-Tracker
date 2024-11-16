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
