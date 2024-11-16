import sys
import json
import os
import datetime

#Define the json file to store tasks

TASKS_FILE = "tasks.json"
class TaskManager:
    def load_tasks():
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        return []

    def save_task(tasks):
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks,file,indent=4)

    def add_task(description):
        tasks = TaskManager.load_tasks()
        task_id  = len(tasks) + 1
        timestamp  = datetime.datetime.now().isoformat()
        new_task = {
            "id" : task_id,
            "description": description,
            "createdAt": timestamp,
            "updatedAt": 0,
            "status": "todo",

        }

        tasks.append(new_task)
        TaskManager.save_task(tasks)
        print(f"Task added successfully (ID: {task_id})")


    def update_task(task_id, new_description):
        tasks = TaskManager.load_tasks()

        for task in tasks:
            if task["id"] == task_id:
                task["description"] == new_description
                task["updated_at"] == datetime.datetime.now().isoformat()
                TaskManager.save_task(tasks)
                print(f"Task {task_id} updated successfully")
        print(f"Task with ID {task_id} not found")


    def delete_task(task_id):
        tasks = TaskManager.load_tasks()
        new_tasks = [task for task in tasks if task["id"]!= task_id]
        TaskManager.save_task(new_tasks)
        print(f"Task {task_id} deleted sucessfully")
    def list_tasks(status=None):
        tasks = TaskManager.load_tasks()
        
        # Filter tasks based on status, or show all tasks if no status is provided
        filtered_tasks = [task for task in tasks if status is None or task["status"] == status]
        
        if not filtered_tasks:
            print("No tasks found")
        else:
            for task in filtered_tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

    def mark_task(task_id,status):

        tasks = TaskManager.load_tasks()

        for task in tasks:
            if task["id"] == task_id:
                task["status"] =status
                task["updatedAt"] == datetime.datetime.now().isoformat()
                TaskManager.save_task(tasks)
                print(f"Task {task_id} marked as {status}")
                return
        print(f"Task {task_id} marked as {status}")
                