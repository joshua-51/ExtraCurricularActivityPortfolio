name = input("Hey what's ur name? ")

while True:
    match name:
        case "Joshua":
            print("You are super cool")
        
        case "q":
            quit()

        case _:
            print("Who?")