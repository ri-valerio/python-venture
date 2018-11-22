# all variables (and even literal values) in python 3 are objects
# and each object has an id associated with its creation

my_int = 7
my_other_int = int(7)
print(type(my_int), my_int, id(my_int))
print(type(my_other_int), my_other_int, id(my_other_int))

print()  # separator

my_float = 7.2
my_other_float = float(7.2)
print(type(my_float), my_float, id(my_float))
print(type(my_other_float), my_other_float, id(my_other_float))

print()  # separator

my_name = "Ricardo"
my_other_name = str("Ricardo")
print(type(my_name), my_name, id(my_name))
print(type(my_other_name), my_other_name, id(my_other_name))

print()  # separator

my_bool1 = 5 > 7
my_bool2 = False or True
my_bool3 = bool(False)
print(type(my_bool1), my_bool1, id(my_bool1))
print(type(my_bool2), my_bool2, id(my_bool2))
print(type(my_bool3), my_bool3, id(my_bool3))

print()  # separator

my_list = [2, 3, 4]
my_other_list = list([2, 3, 4])
print(type(my_list), my_list, id(my_list))
print(type(my_other_list), my_other_list, id(my_other_list))

print()  # separator

my_tuple1 = (5, 6, 7)
my_tuple2 = 5, 6, 7 # parentheses are optional
my_other_tuple = tuple((5, 6, 7))
print(type(my_tuple1), my_tuple1, id(my_tuple1))
print(type(my_tuple2), my_tuple2, id(my_tuple2))
print(type(my_other_tuple), my_other_tuple, id(my_other_tuple))
x, y, _ = my_tuple1 # unpack the tuple but discard the last value
print(x, y)
x, y = y, x # swap the values
print(x, y)

print()  # separator

my_set = {2, 3, 4}
my_other_set = set({2, 3, 4})
print(type(my_set), my_set, id(my_set))
print(type(my_other_set), my_other_set, id(my_other_set))

print()  # separator

my_dict = dict(
    zero  = "nil",
    one   = "first",
    two   = "Second",
    three = "Third"
)
my_other_dict = {
    "zero"  : "nil",
    "one"   : "first",
    "two"   : "Second",
    "three" : "Third"
}
my_mixed_dict = {
        0      : 0,
        "first": "first",
        2      : "second",
        "third": 3
}
print(type(my_dict), my_dict, id(my_dict))
print(type(my_other_dict), my_other_dict, id(my_other_dict))
print(type(my_mixed_dict), my_mixed_dict, id(my_mixed_dict))
