from fileHandlingTasks import checkFile
import sys

def message():  
    MSG = 'For adding tasks: mktsk "Task" "priority (number)" "name of file" \n' \
        'For removing tasks: rmtsk "Task" "name of file"\n' \
        'For reading all the tasks in a file: rdtsk [file]'
    return MSG

def makingSureTasks(userInput):
    global n
    try:
        if userInput[1]:
            n = 1
            return True
        elif userInput[2]:
            n = 2
            return True
        elif userInput[3]:
            n = 3
            return True
        else: n = 0
    except IndexError:
        print(message())

def decipheringInput(userInput):
    makingSureTasks(userInput)
    if n == 4 and "mktsk" == userInput[1] and isinstance(userInput[3], int) and checkFile(userInput[4] == True):
        return ["mktsk", [userInput[3], userInput[2], userInput[4]]]
    
    elif n == 3 and "rmtsk" == userInput[1] and checkFile(userInput[3]):
        return ["rmtsk", [userInput[2], userInput[3]]]
    
    elif n == 2 and "rdtsk" == userInput[1] and checkFile(userInput[2] == True):
        return ["rdtsk", userInput[2]]
    
    else:
        return False