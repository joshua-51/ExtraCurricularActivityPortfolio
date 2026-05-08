import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(sys.argv[1]) as infile:
            reader = csv.DictReader(infile)
            data = []
            for row in reader:
                last, first = row["name"].split(", ")
                data.append({"first": first, "last": last, "house": row["house"]})

        with open(sys.argv[2], "w", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
