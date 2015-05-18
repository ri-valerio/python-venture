#!/usr/bin/python3

def main():
	num 	  = 44
	other_num = 7

	print("Simple Division: "  , type(num / other_num), num / other_num)
	print("Integer Division: " , type(num // other_num), num // other_num)
	print("Modulus Division: " , type(num % other_num), num % other_num)
	print("Round Division: "   , type(round(num / other_num, 4)), round(num / other_num, 4))


	    # to know more about the method that are possible to use
	    # with dictionaries, I should definitely go and hack inside the
	    # IDLE
	    # or search the docs of course

if __name__ == '__main__': main()

