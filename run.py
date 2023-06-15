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
    name = input("Enter task name: ")
    due_date = input("Enter due date: ")
    notes = input("Enter additional notes: ")

    task = {
        "name": name,
        "due_dates": due_date,
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
        status = "Completed" if task ["completed"] else "Not Completed"
        print(f"\nTask #{index+1}")
        print("Name:", task["name"])
        print("Due Date:", task["due_date"])
        print("Notes:", taks["notes"])
        print("Status:", status)
    


# def complete_task():

# def save_task():

# def load_task():

def main():
    display_menu()
    # add_task()
    # view_task()

main()