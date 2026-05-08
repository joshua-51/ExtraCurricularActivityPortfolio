import sys
from datetime import date

class today:
    today = date.today()
    month = today.month
    day = today.day

def msg():
    MSG = "python3 tasks.py [add/remove] [task] [time (hours:mins) (only if add)] \npython3 tasks.py [read]"
    
    sys.exit(MSG)

def checkTime(time):
    #If the time given by the user is "1:20"
    #This returns 1 hr 20 mins
    time = time.split(":")
    if len(time) == 2:
        hours, mins = time
        try:
            hours = int(hours)
            mins = int(mins)
        except Exception:
            return False
        
        if mins > 59:
            hrs = mins // 60
            minutes = mins % 60
            hours = hours + hrs
            if minutes == 0:
                return f"{hours} hrs"
            elif minutes == 1:
                return f"{hours} hrs 1 min"
            else:
                return f"{hours} hrs {minutes} mins"
        else: return f"{hours} hrs {mins} mins"
    else:
        try:
            mins = time[0]
            mins = int(mins)
        except Exception:
            return False
        if mins > 59:
            hrs = mins // 60
            minutes = mins % 60
            hours = hrs
            if minutes == 0:
                return f"{hours} hrs"
            
            else:
                return f"{hours} hrs {minutes} mins"
        else:
            if mins == 1:
                return f"1 min"
            else:
                return f"{mins} mins"

def addTask(task, time=None):
    if time != None:
        if isinstance(task, str):
            task = task.strip().capitalize()
            with open("tasks.csv", "a") as tasks:
                tasks.write(f"{today.month}/{today.day},{task},{time}\n")
                return True
    elif time == None:
        with open("tasks.csv", "a") as tasks:
            task.strip().capitalize()
            tasks.write(f"{today.month}/{today.day}, {task}\n")
            return True
    else:
        msg()

def removeTask(task):
    try:
        with open("tasks.csv", "r") as f:
            OrigTasks = f.readlines()
        with open("tasks.csv", "w") as f:
            for tsk in OrigTasks:
                if task not in tsk:
                    f.write(tsk)
    except Exception:
        msg()

def readTasks():
    with open("tasks.csv", "r") as f:
        unformatted = f.readlines()
        for task in unformatted:
            if len(task.split(",")) == 3:
                DATE, TASK, TIME = task.strip().split(",")
                TASK = TASK.strip()
                print(f" - {DATE} | {TASK} | {TIME}")
            elif len(task.split(",")) == 2:
                DATE, TASK = task.strip().split(",")
                TASK = TASK.strip()
                print(f" - {DATE} | {TASK}")
        return True

def main():
    argv = len(sys.argv) -1
    if argv == 0:
        msg()
    elif argv == 1 and sys.argv[1] == "read":
        readTasks()
    elif argv == 2:
        if sys.argv[1] == "add":
            addTask(sys.argv[2])
        elif sys.argv[1] == "remove":
            removeTask(sys.argv[2])
        else:
            msg()
    elif argv == 3 and sys.argv[1] == "add" and checkTime(sys.argv[3]) != False:
        addTask(sys.argv[2], checkTime(sys.argv[3]))
    else:
        msg()

if __name__ == "__main__":
    main()