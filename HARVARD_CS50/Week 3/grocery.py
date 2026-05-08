grocery_list = {}

while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        for item in sorted(grocery_list.keys()):
            print(f"{grocery_list[item]} {item}")
        break
