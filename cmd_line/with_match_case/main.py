#included file read and write, pre-requisite is to have files being present before running the code
print("""
_________________________________________________________________
             Welcome to the ToDo Task Manager app 
_________________________________________________________________
""")
#reads the file, splits into list based on \n
def reader(filepath):
    with open(filepath, "r") as file:
        tasks = file.read().split("\n")
    print("Tasks loaded from: " + filepath)
    return list(filter(None, tasks)) #Filters blank list item if any

#writes the data into file, by adding \n at end of each list item
def writer(filepath, tasks):
    with open(filepath, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks written to file: " + filepath)
def display_available_tasks(tasks):
    print(f"""
_________________________________________________________________
             Below are the available tasks: 
_________________________________________________________________
""")
    for index, i in enumerate(tasks):
        print(f"{index + 1}. {i}")
#load data
todos = reader("todos.txt")
completed_tasks = reader("completed.txt")

#I have just used list index to find and edit the tasks, which is enough to handle simple task app with lesser code and data
while True:
    user_action = ((input("What do you want to do?\n 1. Add\n 2. Show\n 3. Update\n 4. Complete \n 5. Exit\n \n  : ")).lower()).strip()
    match user_action:
        case "add" | "1" | "a":
            todo = (input("Add new task : ")).capitalize()
            todos.append(todo)
        case "show" | "display" | "2" | "s":
            display_available_tasks(todos)
        case "update" | "3" | "u":
            display_available_tasks(todos)
            task_id = int(input("Enter task ID (Only integers allowed): "))-1 #index management
            todos[task_id] = (input("Enter updated task: ")).capitalize()
        case "complete" | "4" | "c":
            display_available_tasks(todos)
            task_id = int(input("Enter task ID (Only integers allowed): ")) - 1  # index management
            completed_tasks.append(todos[task_id])
            print(f"below task is completed and removed from to-do list: \n {todos[task_id]}\n")
            todos.pop(task_id)
        case "exit" | "5" | "e":
            break

# reupdate the file with tasks
writer("todos.txt", todos)
writer("completed.txt", completed_tasks)


print("Thanks for using the cmd line task manager app \n   Byeeee!!!!")

