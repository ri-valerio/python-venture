#!/usr/bin/python3

# there is no fucking switch in python
# omg - hope it has something better then

def main():
	my_dict  = dict(
		one   = "first",
		two   = "Second",
		three = "Third"
	)

	print(my_dict["one"])

	# a clever away of catch some error/exception
	print(my_dict.get("seven", "other default value"))



if __name__ == "__main__": main()
