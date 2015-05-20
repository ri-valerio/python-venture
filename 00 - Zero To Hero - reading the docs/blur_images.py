#!/usr/bin/python

from PIL import Image, ImageFilter

def main():

    try:
        # Load an image from the hard drive
        original = Image.open("calvin.png")

        # Blur the image
        blurred = original.filter(ImageFilter.BLUR)

        # Display both images
        original.show()
        blurred.show()

        # save the new image
        blurred.save("blurred.png")

    except Exception as e:
        print("Unable to load image", e)

if __name__ == '__main__':
    main()
