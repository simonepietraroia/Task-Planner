import json

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
    task-name = input("Enter task name: ")
    due-date = input("Enter due date: ")
    notes = input("Enter additional notes: ")

    task = {
        "name" = task-name,
        "due_dates": due_date,
        "notes": notes,
        "completed": False
    }

# def view_task():

# def complete_task():

# def save_task():

# def load_task():

def main():
    display_menu()
    add_task()

main()