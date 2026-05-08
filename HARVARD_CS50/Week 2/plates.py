def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 2: Check length (2 to 6 characters)
    if not (2 <= len(s) <= 6):
        return False

    # Rule 1: Must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Rule 5: No periods, spaces, or punctuation
    if not s.isalnum():
        return False

    # Rule 3 & 4: Numbers must be at the end and first number can't be '0'
    for i in range(len(s)):
        if s[i].isdigit():
            # Rule 4: Check if first number is '0'
            if s[i] == '0':
                return False

            # Rule 3: Check if any letters follow this number
            if not s[i:].isdigit():
                return False

            # If we found the first valid number, we can stop the loop
            break

    return True

main()
