import arithmeticCalc
import exponentCalc
import sintancosCalc
print("Hello! This is an interactive calculator!", end="\n\n")

def errormessage():
    print('Enter a valid numerical float')

while True:
    user_input = ("Do you want to add(a), "
    "subtract(b), \n"
    "multiply(c), \n"
    "divide(d), \n"
    "multiply a number by itself n times (e), \n"
    "nth root a number(f), \n"
    "get the sine of a degree(g), \n"
    "get the cosine of a degree(h), or, \n"
    "get the tangent of a degree(i), \n"
    "q to quit")

    match user_input:
        case "a":
            while True:
                try:
                    x = float(input("Enter x in x+y: "))
                    y = float(input("Enter y in x+y: "))
                    break
                except:
                    errormessage()
            arithmeticCalc.add(x,y)
        
        case "b":
            while True: 
                try:
                    x = float(input("Enter x in x-y: "))
                    y = float(input("Enter y in x-y: "))
                    break
                except:
                    errormessage()
            arithmeticCalc.subtract(x,y)

        case "c":
            while True: 
                try:
                    x = float(input("Enter x in x*y: "))
                    y = float(input("Enter y in x*y: "))
                    break
                except:
                    errormessage()
            arithmeticCalc.multiply(x,y)

        case "d":
            while True: 
                try:
                    x = float(input("Enter x in x/y: "))
                    y = float(input("Enter y in x/y: "))
                    break
                except:
                    errormessage()
            arithmeticCalc.divide(x,y)

        case "e":
            while True: 
                try:
                    x = float(input("Enter x in x^y: "))
                    y = float(input("Enter y in x^y: "))
                    break
                except:
                    errormessage()
            exponentCalc.tothepowerof(x,y)

        case "f":
            while True: 
                try:
                    x = float(input("Enter n in nth root of y: "))
                    y = float(input("Enter y in nth root of y: "))
                    break
                except:
                    errormessage()
            exponentCalc.nthrootof(x,y)

        case "g":
            while True: 
                try:
                    x = float(input("Enter the degree that you want to find the sine of: "))
                    break
                except:
                    errormessage()
            sintancosCalc.sinof(x)

        case "h":
            while True: 
                try:
                    x = float(input("Enter the degree that you want to find the cosine of: "))
                    break
                except:
                    errormessage()
            sintancosCalc.cosof(x)

        case "i":
            while True: 
                try:
                    x = float(input("Enter the degree that you want to find the tangent of: "))
                    break
                except:
                    errormessage()
            sintancosCalc.tanof(x)
