todos = []
#included file read and write 
file = open("todos.txt", "r")
print(file)
todos = file.read().splitlines()
file.close()
todos = list(todos)
completed_tasks = []
#I have just used list index to find and edit the tasks, which is enough to handle simple task app with lesser code and data
while True:
    user_action = ((input("What do you want to do?\n 1. Add\n 2. Show\n 3. Update\n 4. Complete \n 5. Exit\n \n  : ")).lower()).strip()
    match user_action:
        case "add" | "1" | "a":
            todo = (input("Add new task : ")).capitalize()
            todos.append(todo)
        case "show" | "display" | "2" | "s":
            for index, i in enumerate(todos):
                print(f"{index+1}. {i}")
        case "update" | "3" | "u":
            for index, i in enumerate(todos):
                print(f"{index+1}. {i}")
            task_id = int(input("Enter task ID (Only integers allowed): "))-1 #index management
            todos[task_id] = (input("Enter updated task: ")).capitalize()
        case "complete" | "4" | "c":
            for index, i in enumerate(todos):
                print(f"{index+1}. {i}")
            task_id = int(input("Enter task ID (Only integers allowed): ")) - 1  # index management
            completed_tasks.append(todos[task_id])
            todos.pop(task_id)
        case "exit" | "5" | "e":
            break
file = open("todos.txt", "w")
for todo in todos:
        file.write(todo + "\n")
file.close()
print("Bye!")

