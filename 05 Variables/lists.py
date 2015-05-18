#!/usr/bin/python3

def main():
    my_list_of_integers             		 = [1, 2, 3]
    my_list_of_strings              		 = ["you", "and", "me"]
    my_list_of_strings_and_integers          = ["I", "love", "you", 4, "ever"]
    my_list_of_strings_integers_and_booleans = ["I", "love", "you", 4, "ever", True]

    print(my_list_of_integers)
    print(my_list_of_strings)
    print(my_list_of_strings_and_integers)

    print() # separator

    print(my_list_of_integers[0])
    print(my_list_of_strings[0])
    print(my_list_of_strings_and_integers[3])
    print( "It is true!" if my_list_of_strings_integers_and_booleans[5] else "Lier")


    # to know more about the method that are possible to use
    # with lists, I should definitely go and hack inside the
    # IDLE
    # or search the docs of course

if __name__ == '__main__': main()
