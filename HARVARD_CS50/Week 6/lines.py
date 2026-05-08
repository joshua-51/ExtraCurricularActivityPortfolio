import sys

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        count = 0
        for line in lines:
            # Strip whitespace to check if line is empty or a comment
            stripped = line.lstrip()
            if stripped and not stripped.startswith("#"):
                count += 1
        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
