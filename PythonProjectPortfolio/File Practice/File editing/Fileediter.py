file_path = "my_file.txt"

def delete_everything():
    ask = input('what document do you want to delete?(enter the extension as well) ')
    try:
        with open(ask, 'r+') as f:
            f.seek(0)  # Move the file pointer to the beginning of the file
            f.truncate()  # Truncate the file from the current position (beginning)
    except:
        print("you need to enter the name of a correct file")

def add_something():
    ask = input('what do file do you want to add content to?(add the extension of the file too)? ')
    content = input("What do you want to be entered in the file?")
    try:
        with open(ask, "a") as file:
            file.write(content)
    except:
        print("Enter the name of a correct file!")

def create_new_file():
    file_name = input("enter your file's name(add an extension) ")
    with open(file_name, "w") as new:
        pass

while True:
    ask_what_do = input('Create new file(w), edit a file(a), delete an existing file(d), or quit(q)')
    if ask_what_do == "w":
        create_new_file()
    elif ask_what_do == "a":
        add_something()
    elif ask_what_do == "d":
        delete_everything()
    elif ask_what_do == "q":
        quit()
    else:
        print('Enter a valid answer!')
