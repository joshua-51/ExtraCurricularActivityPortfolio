def createFiles(fileName):
    try:
        with open(fileName, 'x') as file:
            file.write("")
    except FileExistsError:
        print(f"{fileName} already exists!")
    except Exception as e:
        print(f"{e} occured")

def deleteAllContent(fileName):
    try:
        with open(fileName, 'w') as file:
            file.write("")
    except Exception as e:
        print(f'{e} occured')

def rdGrades(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.readlines
            
    except Exception:
        print("file doesn't exist")