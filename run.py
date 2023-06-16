import json

tasks = []

def display_menu():
    """
    This function displays the different task options that 
    this application provides.
    """
    print("-----Task-Planner-----")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task As Complete")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")

def add_task():
    """
    This function allows the user to input the name, due-date, and 
    additional notes/description step by step
    """
    name = input("Enter task name:\n")
    due_date = input("Enter due date:\n")
    notes = input("Enter additional notes:\n")
    
    task = {
        "name": name,
        "due_date": due_date,
        "notes": notes,
        "completed": False
    }
    
    tasks.append(task)
    print("Task added successfully.")

def view_task():
    """
    This function searches the tasks variable for previously recorded tasks and displays them for the user.
    if there are none then it will alert the user"
    """
    if len(tasks) == 0:
        print("No tasks found.")
        return
    
    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"\nTask #{index+1}")
        print("Name:", task["name"])
        print("Due Date:", task["due_date"])
        print("Notes:", task["notes"])
        print("Status:", status)
        
def complete_task():
    """
    This function searches if there are tasks and shows the user the tasks that are saved
    and prompt the user to input the number of the task to mark it as complete
    """
    if len(tasks) == 0:
        print("No tasks found.")
        return

    view_task()

    try:
        index = int(input("Enter the task number to mark as complete:\n")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return
        
        tasks[index]["completed"] = True
        print("Task mark as complete.")
    except ValueError:
        print("Invalid input.")

def save_task():
    """
    This function takes all the information currently stores in the tasks
    variable and saves it to the tasks.json file
    """
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        print("Tasks successfully saved.")

def load_task():
    """
    The function takes the perviously created and saved tasks and assigns them to the 
    tasks variable from the tasks.json file. This must be used when starting up the program to load previous tasks.
    """
    try:
        with open("tasks.json", "r") as file:
            loaded_tasks = json.load(file)
            tasks.clear()
            tasks.extend(loaded_tasks)

        print("Tasks loaded from file.")
    except FileNotFoundError:
        print("No saved tasks found.")

def main():
    while True:
        display_menu()
        choice = input("enter your choice (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            save_task()
        elif choice == "5":
            load_task()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()