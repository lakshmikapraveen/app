def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

def add_task(tasks):
    """Add a new task to the to-do list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.\n")

def remove_task(tasks):
    """Remove a task from the to-do list by its number."""
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from your to-do list.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid task number.\n")

def todo_list():
    tasks = []
    
    print("Welcome to the To-Do List App!")
    
    while True:
        print("Options:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    todo_list()
