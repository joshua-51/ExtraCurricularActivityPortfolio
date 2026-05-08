months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            m, d, y = date.split("/")
        elif "," in date:
            m_name, d_year = date.split(" ", 1)
            d, y = d_year.split(", ")
            m = months.index(m_name) + 1
        else:
            continue

        if int(m) > 12 or int(d) > 31:
            continue

        print(f"{int(y):04}-{int(m):02}-{int(d):02}")
        break
    except (ValueError, IndexError):
        pass
