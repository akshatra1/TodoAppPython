# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added: " + task)

# Function to delete a task
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task deleted: " + task)
    else:
        print("Task not found")

# Function to display tasks
def show_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to delete: ")
        delete_task(task)
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
