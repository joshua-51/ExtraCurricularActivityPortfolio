# 1. Ask the user what they want to name the file
filename = input("Enter the name for your new file (e.g., notes.txt): ")

# Ensure the filename ends with .txt
if not filename.endswith(".txt"):
    filename += ".txt"

# 2. Ask the user for the content
print("Enter the text you want to save. Type 'SAVE' on a new line to finish:")

lines = []
while True:
    line = input()
    if line.strip().upper() == "SAVE":
        break
    lines.append(line)

# 3. Write the information to the file
try:
    # The 'with' statement handles closing the file automatically
    with open(filename, "w") as file:
        file.write("\n".join(lines))
    
    print(f"\nSuccessfully created '{filename}' with your info!")

except Exception as e:
    print(f"An error occurred: {e}")