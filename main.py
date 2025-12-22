todos = []
#I have just used list index to find and edit the tasks, which is enough to handle simple task app with lesser code and data
while True:
    user_action = ((input("What do you want to do?\n 1. Add\n 2. Show\n 3. Update\n 4. Exit\n \n  : ")).lower()).strip()
    match user_action:
        case "add" | "1" | "a":
            todo = f"{len(todos)+1}. "+(input("Add new task : ")).capitalize()
            todos.append(todo)
        case "show" | "display" | "2" | "s":
            for i in todos:
                print(i)
        case "update" | "3" | "u":
            for i in todos:
                print(i)
            task_id = int(input("Enter task ID (Only integers allowed: "))-1 #index management
            todos[task_id] = f"{task_id}. "+(input("Enter updated task: ")).capitalize()
        case "exit" | "3" | "e":
            break
print("Bye!")

