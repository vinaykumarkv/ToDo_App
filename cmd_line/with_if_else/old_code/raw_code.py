all_tasks = {}
completed_tasks = {}
incomplete_tasks = {}

while True:
    print("""
    To-do task manager
    Below are the current available tasks
    """)

    activity = input("""
    What would you like to do? 
    1. Add new task
    2. Delete task
    3. Edit task
    4. Mark task as completed
    5. Mark task as incomplete
    
    : """)

    if activity == '1':
        max_key = max(all_tasks, default=0)
        new_task = input("""
                         Enter new task: """)
        all_tasks[max_key+1] = new_task
        print("Below are the current available tasks:")
        for key in all_tasks:
            print(key, ":", all_tasks[key])
        print("Below are the completed tasks:")
        for key in completed_tasks:
            print(key, ":", completed_tasks[key])
        print("Below are the incomplete tasks:")
        for key in incomplete_tasks:
            print(key, ":", incomplete_tasks[key])
    elif activity == '2':
        key_to_delete = int(input("""
                             Enter task to be deleted: """))
        del all_tasks[key_to_delete]
        all_tasks = {i: v for i, v in enumerate(all_tasks.values(), 1)}
        print("Below are the current available tasks:")
        for key in all_tasks:
            print(key, ":", all_tasks[key])
        print("Below are the completed tasks:")
        for key in completed_tasks:
            print(key, ":", completed_tasks[key])
        print("Below are the incomplete tasks:")
        for key in incomplete_tasks:
            print(key, ":", incomplete_tasks[key])
    elif activity == '3':
        task_to_edit = int(input("""
                             Enter task to be edited: """))

        all_tasks[task_to_edit] = input("""
                                        Please enter updated description for the task: """)
        dict(sorted(all_tasks.items()))
        print("Below are the current available tasks:")
        for key in all_tasks:
            print(key, ":", all_tasks[key])
        print("Below are the completed tasks:")
        for key in completed_tasks:
            print(key, ":", completed_tasks[key])
        print("Below are the incomplete tasks:")
        for key in incomplete_tasks:
            print(key, ":", incomplete_tasks[key])
    elif activity == '4':
        max_key = max(completed_tasks, default=0)
        task_to_be_completed = input("""
                                     Please enter task to be marked completed: """)
        completed_tasks[max_key+1] = all_tasks[task_to_be_completed]
        del all_tasks[task_to_be_completed]
        all_tasks = {i: v for i, v in enumerate(all_tasks.values(), 1)}
        print("Below are the current available tasks:")
        for key in all_tasks:
            print(key, ":", all_tasks[key])
        print("Below are the completed tasks:")
        for key in completed_tasks:
            print(key, ":", completed_tasks[key])
        print("Below are the incomplete tasks:")
        for key in incomplete_tasks:
            print(key, ":", incomplete_tasks[key])
    elif activity == '5':
        max_key = max(incomplete_tasks, default=0)
        task_to_incomplete = input("""
                                         Please enter task to be marked completed: """)
        incomplete_tasks[max_key + 1] = all_tasks[task_to_incomplete]
        del all_tasks[task_to_incomplete]
        all_tasks = {i: v for i, v in enumerate(all_tasks.values(), 1)}

        print("Below are the current available tasks:")
        for key in all_tasks:
            print(key, ":", all_tasks[key])
        print("Below are the completed tasks:")
        for key in completed_tasks:
            print(key, ":", completed_tasks[key])
        print("Below are the incomplete tasks:")
        for key in incomplete_tasks:
            print(key, ":", incomplete_tasks[key])
    else:
        print("Invalid activity!!")