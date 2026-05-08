import numpy as np

def sinof(degrees):
    radians = np.radians(degrees)
    sine = np.sin(radians)
    print(f"the sine of {degrees} is {sine}")

def cosof(degrees):
    radians = np.radians(degrees)
    cosine = np.cos(radians)
    print(f"the cosine of {degrees} is {cosine}")

def tanof(degrees):
    radians = np.radians(degrees)
    tangent = np.tan(radians)
    print(f"the tangent of {degrees} is {tangent}")

