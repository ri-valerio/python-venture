#!/usr/bin/python

import cImage as image


def main():
    img = image.Image("calvin.png")

    win = image.ImageWin(img.getWidth(), img.getHeight())
    img.draw(win)

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            new_red = 255 - p.getRed()
            new_green = 255 - p.getGreen()
            new_blue = 255 - p.getBlue()

            new_pixel = image.Pixel(new_red, new_green, new_blue)

            img.setPixel(col, row, new_pixel)

    img.draw(win)
    win.exitonclick()

    print(img.getWidth())
    print(img.getHeight())

    p = img.getPixel(25, 55)
    print(p.getRed(), p.getGreen(), p.getBlue())


if __name__ == '__main__': main()
