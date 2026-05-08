import sys

def message():
    print("Usage: python project.py [add/view/delete] [priority] [task]")

def getting_input(args):
    if len(args) < 2:
        message()
        return None
    command = args[1].lower().strip()
    if command not in ['add', 'view', 'delete']:
        message()
        return None
    if command == 'add':
        if len(args) < 4:
            message()
            return None
        priority = args[2]
        task = ' '.join(args[3:])
        return (command, priority, task)
    elif command in ['view', 'delete']:
        if len(args) < 3:
            message()
            return None
        task = ' '.join(args[2:])
        return (command, task)