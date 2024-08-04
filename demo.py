
tasks = []

def display_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    display_tasks()
    task_number = int(input("Enter the task number to delete: "))
    try:
        tasks.pop(task_number - 1)
        print("Task deleted!")
    except IndexError:
        print("Invalid task number.")

while True:
    print("\nOptions:")
    print("1. Display tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

