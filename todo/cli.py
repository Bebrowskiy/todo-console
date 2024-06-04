import sys
from todo.tasks import add_task, list_tasks, remove_task


def main():
    if len(sys.argv) < 2:
        print("Usage: todo <command> [arguments]")
        print("Commands:")
        print("  add <task>        Add a new task")
        print("  list              List all tasks")
        print("  remove <task_id>  Remove a task by its ID")
        return

    command = sys.argv[1]

    if command == "add":
        task = " ".join(sys.argv[2:])
        add_task(task)
    elif command == "list":
        list_tasks()
    elif command == "remove":
        try:
            task_id = int(sys.argv[2])
            remove_task(task_id)
        except (IndexError, ValueError):
            print("Please provide a valid task ID to remove.")
    else:
        print(f"Invalid command: {command}")


if __name__ == "__main__":
    main()
