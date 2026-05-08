def get_names():
    userinput = input("Enter names separated by commas - like this - name, name, name: ")
    global names_list
    names_list = []
    for name in userinput.split(", "):
        names_list.append(name.strip().title())
    names_list = [name for name in names_list if name]
    print(end="\n\n")
    return names_list
def alphabetize(listOfStrings):
    return sorted(listOfStrings)
def presentation(object):
    if object == list:
        for i in object:
            print()
            print(object)
            print()
def listToWords(list):
    for l in list:
        print(l + ", ", end="")
def main():
    print(listToWords(alphabetize(get_names())))