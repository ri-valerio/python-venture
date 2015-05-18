#!/usr/bin/python3

def main():
	# there are two ways of creating an dictionary:

	# this way:
	my_dict_of_integers = {0 : 12, 1 : 2, 2 : 5}
	my_other_dict_of_integers = {"zero" : 12, "one" : 2, "two" : 5}

	my_dict_of_strings = { 0: "Ricardo", 1: "Sílvia"}
	my_other_dict_of_strings = { "r": "Ricardo", "s": "Sílvia"}


	# and this way:
	my_dict_of_search_engines = dict(
		google = "http://www.google.com",
		duckgo = "http://www.duckgo.com",
		yahoo  = "http://www.yahoo.com"
	)
	# add another value to the dictionary
	my_dict_of_search_engines["bing"] = "http://www.bing.com"

	print(type(my_dict_of_integers), my_dict_of_integers)
	print(type(my_dict_of_integers[0]), my_dict_of_integers[0])

	print(type(my_other_dict_of_integers), my_other_dict_of_integers)
	print(type(my_other_dict_of_integers["zero"]), my_other_dict_of_integers["zero"])

	print(type(my_dict_of_strings), my_dict_of_strings)
	print(type(my_dict_of_strings[1]), my_dict_of_strings[1])

	print(type(my_other_dict_of_strings), my_other_dict_of_strings)
	print(type(my_other_dict_of_strings["r"]), my_other_dict_of_strings["r"])

	print(type(my_dict_of_search_engines), my_dict_of_search_engines)
	print(type(my_dict_of_search_engines["google"]), my_dict_of_search_engines["google"])

    # to know more about the method that are possible to use
    # with dictionaries, I should definitely go and hack inside the
    # IDLE
    # or search the docs of course


if __name__ == '__main__': main()
