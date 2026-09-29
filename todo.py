tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def add_task():
    task = input("\nEnter a task: ")

    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully!")


def delete_task():
    if not tasks:
        print("\nNo tasks to delete.")
        return

    show_tasks()

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print(f"Deleted: {deleted_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("\nThank you for using the To-Do List!")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, 3, or 4.")