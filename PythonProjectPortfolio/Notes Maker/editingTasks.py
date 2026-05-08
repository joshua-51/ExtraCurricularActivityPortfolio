def removeTask(TASK, file):
    edited_tasks = []
    
    if determine(file) == False:
        return False
    else:
        pass

    with open (f"{file}", "r") as tasks:
        tasks = tasks.readlines()
        for task in tasks:
            if TASK in task:
                pass
            else: edited_tasks.append(task)
        if edited_tasks == tasks:
            return False
    with open (f"{file}", "w"):
        for task in edited_tasks:
            file.write(edited_tasks)
                
def makeTask(TASK, priority, file):
    if determine(file) == False:
        return False
    else:
        pass
    with open (file, "a") as f:
        f.write(f"{priority},{TASK}")

def readTasks(file):
    if determine(file) == False:
        return False
    with open(file, "r") as f:
        tasks = f.readlines()
        return tasks

def determine(file):
    try:
        with open(f"{file}", "r") as f:
            return True
    except Exception:
        return False