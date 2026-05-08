def main():
    time = input("What time is it? ").strip()

    # Use the convert function to get the time as a float
    hours = convert(time)

    # Check the time ranges
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = time.split(":")

    # Convert minutes to a fraction of an hour (e.g., 30 mins = 0.5 hours)
    new_minutes = float(minutes) / 60

    # Return the total time as a float
    return float(hours) + new_minutes

if __name__ == "__main__":
    main()
