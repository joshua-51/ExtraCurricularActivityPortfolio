import math

def tothepowerof(x,y):
    print(f'{x} ^ {y} =', float(x**y))

def nthrootof(index, under):
    nth_root = math.pow(under, 1/index)
    print(f"The {index}'th root of {under} is {nth_root}")
