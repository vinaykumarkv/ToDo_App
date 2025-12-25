import time
import os


FILEPATH = "todo_list.txt"
if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as file:
        pass

def get_todos(filepath=FILEPATH):
    """Read in a text file and return a list of tasks.
    Please provide the filepath to the text file that contains the tasks"""
    with open(filepath, "r") as file:
        tasks = file.readlines()
    print("Tasks loaded from: " + filepath)
    return tasks

#writes the data into file, by adding \n at end of each list item
def write_todos(tasks,filepath=FILEPATH):
    """Write tasks to a text file.
    Please provide the filepath to the text file where tasks should be written"""
    with open(filepath, "w") as file:
        file.writelines(tasks)
    print("Tasks written to file: " + filepath)
def display_available_tasks(tasks):
    """Display the available tasks."""
    print(f"""
_________________________________________________________________
             Below are the available tasks: 
_________________________________________________________________
""")
    for index, i in enumerate(tasks):
        print(f"{index + 1}. {i}")

def get_time():
    """Return the current date and time."""
    return time.strftime("%d-%m-%Y %H:%M:%S")