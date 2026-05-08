def addClass(ClassName):
    try:
        with open(f"{ClassName}.csv", "x") as file:
            file.write("")
    except FileExistsError:
        print("Class already exists")

def addNameGrade(Class, Name, Grade, Outof):
    if isinstance(Grade, float) == True and isinstance(Outof, float) == True:
        Grade = Grade/Outof
        Grade = Grade*100
    else:
        return False

    try:
        with open(f"{Class}.csv", "a") as clas:
            clas.write(f"{Name},{Grade}")
            return True
    except Exception:
        return False

def removeName(Class, Name):
    try:
        with open(f"{Class}.txt", "r+") as clas:
            names = clas.readlines()
            names = [item.split(',')[0] for item in names]
            for name in names:
                if name == Name:
                    pass
                    
            

    except Exception:
        return False

