from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("cat.gif") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save("OutlinCat.jpeg")



main()