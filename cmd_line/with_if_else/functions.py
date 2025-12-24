import time


#reads the file, splits into list based on \n
def reader(filepath):
    """Read in a text file and return a list of tasks.
    Please provide the filepath to the text file that contains the tasks"""
    with open(filepath, "r") as file:
        tasks = file.read().split("\n")
    print("Tasks loaded from: " + filepath)
    return list(filter(None, tasks)) #Filters blank list item if any

#writes the data into file, by adding \n at end of each list item
def writer(filepath, tasks):
    """Write tasks to a text file.
    Please provide the filepath to the text file where tasks should be written"""
    with open(filepath, "w") as file:
        for task in tasks:
            file.write(task + "\n")
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