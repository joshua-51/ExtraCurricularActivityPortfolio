
def makeFile(file):
    with open(file, "w"):
        pass

def checkFile(file):
    try:
        with open(file, "r"):
            return True
    except Exception:
        return False