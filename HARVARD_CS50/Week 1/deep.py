answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Clean the input: remove whitespace and make it lowercase
answer = answer.strip().lower()

# Check if the answer matches any of the accepted forms
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
