def add_task(tasks, description):
    max_key = max(tasks.keys(), default=0)
    tasks[max_key + 1] = description
    return tasks

def delete_task(tasks, key_to_delete):
    if key_to_delete in tasks:
        del tasks[key_to_delete]
        # Re-index keys 1, 2, 3...
        return {i: v for i, v in enumerate(tasks.values(), 1)}
    return tasks

def update_task(tasks, key_to_update):
    if key_to_update in tasks:
        tasks[key_to_update] = input("Add new task description")
        # Re-index keys 1, 2, 3...
        return {i: v for i, v in enumerate(tasks.values(), 1)}
    return tasks

def mark_status(source_tasks, target_tasks, key):
    if key in source_tasks:
        max_target = max(target_tasks.keys(), default=0)
        target_tasks[max_target + 1] = source_tasks[key]
        del source_tasks[key]
        # Re-index source
        new_source = {i: v for i, v in enumerate(source_tasks.values(), 1)}
        return new_source, target_tasks
    return source_tasks, target_tasks