#!/usr/bin/python3

def main():
    s = 'this is a string'
    print("capitalize: ", s.capitalize())
    print("title: ", s.title())
    print("upper: ", s.upper())
    print("swapcase: ", s.swapcase())
    print("find: ", s.find('is'))
    print("replace: ", s.replace('this', 'that'))
    print("strip: ", s.strip())
    print("isalnum: ", s.isalnum())
    print("isalpha: ", s.isalpha())
    print("isdigit: ", s.isdigit())
    print("isprintable: ", s.isprintable())

if __name__ == "__main__": main()

