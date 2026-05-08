import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # \b is a word boundary, ensuring "um" isn't part of another word
    # re.IGNORECASE makes it catch "Um" and "UM"
    find_um = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(find_um)

if __name__ == "__main__":
    main()
