import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

target = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
