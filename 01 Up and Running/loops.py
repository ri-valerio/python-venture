#
# Example file for working with loops
#


def main():
    x, y = 0, 0

    while x < 5:
        print(x)
        x += 1

    print()  # separator

    # define a while loop
    while (y < 5):
        print(y)
        y = y + 1

    print()  # separator

    # define a for loop
    for x in range(5, 10):
        print(x)

    print()  # separator

    # use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    print()  # separator

    # use the break and continue statements
    for x in range(5, 10):
        # if (x == 7): break
        # if (x % 2 == 0): continue
        print(x)

    print()  # separator

    # using the enumerate() function to get index
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()
