import os
import json

tasks_file = 'tasks.json'


def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, 'r') as f:
        return json.load(f)


def save_tasks(tasks):
    with open(tasks_file, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")


def remove_task(task_id):
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        removed = tasks.pop(task_id - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed}")
    else:
        print("Invalid task ID.")
