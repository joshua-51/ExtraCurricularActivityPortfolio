import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regex to capture hours, minutes (optional), and AM/PM
    if matches := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s):
        parts = list(matches.groups())
        # Standardize minutes to "00" if empty
        if parts[1] == None: parts[1] = "00"
        if parts[4] == None: parts[4] = "00"

        # Check for invalid minutes
        if int(parts[1]) >= 60 or int(parts[4]) >= 60:
            raise ValueError

        return f"{to_24(parts[0], parts[1], parts[2])} to {to_24(parts[3], parts[4], parts[5])}"
    else:
        raise ValueError

def to_24(hour, minute, am_pm):
    hour = int(hour)
    if am_pm == "AM":
        if hour == 12: hour = 0
    else:
        if hour != 12: hour += 12
    return f"{hour:02}:{minute}"

if __name__ == "__main__":
    main()
