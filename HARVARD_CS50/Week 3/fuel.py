while True:
    fraction = input("Fraction: ")
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x <= y:
            percentage = round((x / y) * 100)
            break
    except (ValueError, ZeroDivisionError):
        pass

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
