# Task 2 : Create a To-Do List Application

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file into a list."""
    tasks = []
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass  # No file yet, no tasks
    return tasks

def save_tasks(tasks):
    """Save tasks list to the file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Empty task cannot be added.")

def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    print("=== To-Do List Application ===")

    while True:
        print("\n Choose an option:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
           
        elif choice == "4":
            print("Exiting... Your tasks have been saved.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
