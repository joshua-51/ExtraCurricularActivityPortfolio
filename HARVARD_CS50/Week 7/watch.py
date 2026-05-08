import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Look for src="http(s)://www.youtube.com/embed/ID"
    if match := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"', s):
        return f"https://youtu.be/{match.group(1)}"
    return None

if __name__ == "__main__":
    main()
