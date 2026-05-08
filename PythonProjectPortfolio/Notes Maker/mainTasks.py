import sys
from editingTasks import removeTask
from editingTasks import makeTask
from editingTasks import readTasks
import userInputTasks

USERINPUT = sys.argv
MSG = userInputTasks.message
arguments = userInputTasks.decipheringInput(USERINPUT)
if arguments == False:
    print(MSG)
    sys.exit()
elif arguments[0] == "mktsk":
    priority, task, file = arguments[1][0], arguments[1][1], arguments[1][2]
    makeTask(task, priority, file)
elif arguments[0] == "rmtsk":
    task, file = arguments[1][0], arguments[1][1]
    removeTask(task, file)
elif arguments[0] == "rdtsk":
    file = arguments[1]
    readTasks(file)
else:
    print(MSG)
    sys.exit()