#!/usr/bin/python3

def main():

	#simple string
	s0 = "this is a string"

	# ascii special chars
	s1 = "this is\n a string"

	# "raw" string
	s2 = r"this is\n a string"


	n = 2
	# obsolete way
	s3 = "print the number %d dude!" % n
	# new and best practice way
	s4 = "print the number {} dude!".format(n)

	# the "\" character does the same like c macros
	# this is mostly used in "doc strings"
	s5 = """\
this is a fucking
huge string that
I can break into
many lines as I like...
"""

	# print them all bitch
	print(s0)
	print(len(s0))
	print(s0[2:7]) # from 2 to 6 - because 7 will not appear
	print(s1)
	print(s2)
	print(s3)
	print(s4)
	print(s5)


if __name__ == '__main__':
	main()
