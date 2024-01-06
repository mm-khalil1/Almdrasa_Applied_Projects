"""
# Created by ChatGPT
Task Manager Program

This program allows users to manage tasks through a simple command-line interface.
Users can add tasks, view existing tasks, remove tasks, and exit the program.

Functions:
- show_menu(): Display the program menu and return the user's choice.
- add_task(tasks): Prompt the user to input a task and add it to the tasks list.
- view_tasks(tasks): Display the tasks in the tasks list.
- remove_task(tasks): Remove a task from the tasks list based on user input.

Main Loop:
The main loop continuously prompts the user for their choice and performs the corresponding action.
The loop exits when the user chooses to exit (option 4).

Usage:
Run this script to start the Task Manager program.

Author: OpenAI
Date: December 7, 2023
"""

def show_menu():
    """
    Display a menu for the user to choose a task and return the selected choice.
    """
    print("\nChoose one of the following options:")
    print("1- Add a task")
    print("2- View tasks")
    print("3- Remove a task")
    print("4- Exit")
    return int(input("Enter the corresponding number: "))

def add_task(tasks):
    """
    Prompt the user to input a task and add it to the tasks list.

    Args:
    tasks (list): List of tasks to which the new task will be added.
    """
    task = input("Type the task you want to add: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    """
    Display the tasks in the tasks list.

    Args:
    tasks (list): List of tasks to be displayed.
    """
    if not tasks:
        print("There are no tasks.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(tasks):
    """
    Remove a task from the tasks list based on user input.

    Args:
    tasks (list): List of tasks from which a task will be removed.
    """
    view_tasks(tasks)
    if not tasks:
        print("There are no tasks to remove.")
        return

    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number. No task removed.")

# Main program
tasks = []
while True:
    choice = show_menu()

    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        remove_task(tasks)
    elif choice == 4:
        print("Exiting the Task Manager program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
