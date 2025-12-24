import model


def show_tasks(title, tasks):
    print(f"\n--- {title} ---")
    for key, val in tasks.items():
        print(f"{key}: {val}")


def run_menu():
    all_tasks = {}
    completed = {}

    while True:
        choice = input("\n1. Add  2. Delete  3.Update 4.Complete  5. Exit: ")

        if choice == '1':
            desc = input("Task description: ")
            all_tasks = model.add_task(all_tasks, desc)
        elif choice == '2':
            key = int(input("Task ID to delete: "))
            all_tasks = model.delete_task(all_tasks, key)
        elif choice == '3':
            key = int(input("Task ID to update: "))
            all_tasks = model.update_task(all_tasks, key)
        elif choice == '4':
            key = int(input("Task ID to complete: "))
            all_tasks, completed = model.mark_status(all_tasks, completed, key)
        elif choice == '5':
            break

        show_tasks("Available Tasks", all_tasks)
        show_tasks("Completed Tasks", completed)
