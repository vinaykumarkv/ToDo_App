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
todos = reader("files\\todo_list.txt")
completed_tasks = reader("files\\completed_list.txt")

while True:
    user_action = input("Type add, show, edit, complete or exit and todo item\n :")
    user_action = user_action.lower().strip()
    try:
        if user_action.startswith("add"):
            todo = user_action.replace("add ", "")
            todos.append(todo)

        elif user_action.startswith("show"):
            display_available_tasks(todos)
        elif user_action.startswith("edit"):
            todo = user_action.replace("edit ", "")
            for i in todos:
                if todo in i:
                    todos[todos.index(i)] = f"{input("Please enter new todo item to replace: ")}"
                    found = True
                    break
                else:
                    found = False
                    continue
            if not found:
                print("""
    ------------------------------------------------------------------------------------------
                                 Below are the current Todo items
    ------------------------------------------------------------------------------------------""")
                display_available_tasks(todos)
                index = int(input(f"Unable to find the todo item to edit. please enter the index number of item: "))
                todos[index-1] = f"{input("Please enter new todo item to replace: ")}"

        elif user_action.startswith("complete"):
            todo = user_action.replace("complete ", "")
            for i in todos:
                if todo in i:
                    todos.remove(i)
                    found = True
                    break
                else:
                    found = False
                    continue
            if not found:
                print("""
            ------------------------------------------------------------------------------------------
                                         Below are the current Todo items
            ------------------------------------------------------------------------------------------""")
                for i1 in todos:
                    print(i1)
                index = int(input(f"Unable to find the todo item to complete. please enter the index number of item: "))
                todos.remove(todos[index-1])
        elif user_action.startswith("exit"):
            break
    except ValueError:
        print("Please enter a valid value.")
# reupdate the file with tasks
writer("files\\todo_list.txt", todos)
writer("files\\completed_list.txt", completed_tasks)

print("Thanks for using the cmd line task manager app \n   Byeeee!!!!")