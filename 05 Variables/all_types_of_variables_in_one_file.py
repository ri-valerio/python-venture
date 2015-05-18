#!/usr/bin/python3


# all variables (and even literal values) in python 3 are objects
# and each object has an id associated with its creation

def main():

    my_int   = 7
    my_float = 7.2
    my_name  = "Ricardo"
    my_bool  = 5 > 7 # False/True   -> with Capital-case

    my_list  = [2,3,4]
    my_tuple = (2,3,4)
    my_set   = {2,3,4}
    my_dict  = dict(
    	one   = "first",
    	two   = "Second",
    	three = "Third"
    )
    print("This is the variables.py file.")

    print(type(my_int), my_int, id(my_int))
    print(type(my_float), my_float, id(my_float))
    print(type(my_name), my_name, id(my_name))
    print(type(my_bool), my_bool, id(my_bool))

    print(type(my_list), my_list, id(my_list))
    print(type(my_tuple), my_tuple, id(my_tuple))
    print(type(my_set), my_set, id(my_set))
    print(type(my_dict), my_dict, id(my_dict))


if __name__ == "__main__": main()
