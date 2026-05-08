def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    result = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            result += char
    return result

if __name__ == "__main__":
    main()
