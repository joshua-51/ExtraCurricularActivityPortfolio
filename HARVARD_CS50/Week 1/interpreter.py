expression = input("Expression: ").strip()

# Split the input into three parts based on the spaces
x, y, z = expression.split(" ")

# Convert the numbers from strings to floats
x = float(x)
z = float(z)

# Perform the math based on the operator (y)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Print the result formatted to one decimal place
print(f"{result:.1f}")
