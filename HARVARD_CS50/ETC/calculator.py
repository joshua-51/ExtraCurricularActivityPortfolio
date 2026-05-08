def addition():
    x=float(input("Enter the x in x + y: "))
    y=float(input("Enter the y in x + y: "))
    print(f"{x}+{y} is", x+y)

def subtraction():
    x=float(input("Enter the x in x - y: "))
    y=float(input("Enter the y in x - y: "))
    print(f"{x} - {y} is", x-y)

def multiplication(x,y):
    x=float(input("Enter the x in x * y: "))
    y=float(input("Enter the y in x * y: "))
    print(f"{x} * {y} is", x*y)

def division(x,y):
    x=float(input("Enter the x in x ÷ y: "))
    y=float(input("Enter the y in x ÷ y: "))
    print(f"{x} / {y} is", x/y)
            
def userInput():
    while True: 
        dec = input("What do you want to do, Add, Subtract, Divide, or Multiply?, q to quit ").strip().title()
        if dec == "Add":
            addition()
        elif dec == "Subtract":
            subtraction()
        elif dec == "Multiply":
            multiplication()
        elif dec == "Divide":
            division()
        elif dec == 'Q':
            quit()
        else:
            print("Enter a valid action!")
            continue

userInput()