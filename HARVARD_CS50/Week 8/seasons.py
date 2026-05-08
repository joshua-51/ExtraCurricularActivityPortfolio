import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        # Validate format YYYY-MM-DD
        dob = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    diff = today - dob
    total_minutes = diff.days * 24 * 60

    # Convert to words
    words = p.number_to_words(total_minutes, wantlist=False)
    # Remove 'and', capitalize the start, and add 'minutes'
    output = words.replace(" and ", " ").capitalize()
    print(f"{output} minutes")

if __name__ == "__main__":
    main()
