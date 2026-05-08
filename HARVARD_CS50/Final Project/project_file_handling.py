def file_exists(file):
    try:
        with open(file, 'r'):
            return True
    except FileNotFoundError:
        return False

def add_task(task, file):
    with open(file, 'a') as f:
        f.write(f"{task}\n")

def view_tasks(file):
    if not file_exists(file):
        return False
    with open(file, 'r') as f:
        tasks = f.readlines()
    for task in tasks:
        return task.strip()
    
def delete_task(task, file):
    if not file_exists(file):
        return False
    with open(file, 'r') as f:
        tasks = f.readlines()
    with open(file, 'w') as f:
        for tsk in tasks:
            if tsk.strip() not in task:
                f.write(tsk)