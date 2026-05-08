import sys
import os
from PIL import Image, ImageOps

def main():
    # 1. Validate arguments (length and extensions)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    valid = [".jpg", ".jpeg", ".png"]

    if ext2 not in valid:
        sys.exit("Invalid output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    try:
        # 2. Process images
        shirt = Image.open("shirt.png")
        size = shirt.size

        with Image.open(sys.argv[1]) as user_img:
            # Crop and resize user image to match shirt
            user_img = ImageOps.fit(user_img, size)
            # Paste shirt on top (third argument is the mask for transparency)
            user_img.paste(shirt, shirt)
            user_img.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
