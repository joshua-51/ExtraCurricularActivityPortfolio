import re

def main():
    print(is_valid(input("IPv4 Address: ")))

def is_valid(ip):
    # Regex checks for 4 groups of 1-3 digits separated by dots
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for group in matches.groups():
            if int(group) > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
