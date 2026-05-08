import time
import random

class timing:
    def __init__(self, x, y):
        self.difficulty = (y-x) + x + y

class questions:
    def __init__(self, x, y):
        self.x = random.randint(x,y)
        self.y = random.randint(x,y)
    def addition(self):
        self.ans = self.x + self.y
    def subtraction(self):
        self.ans = self.x - self.y
    def multiplication(self):
        self.ans = self.x * self.y
        