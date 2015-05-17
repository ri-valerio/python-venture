#!/usr/bin/python3

try:
	fh = open('xlines.txt')
	for line in fh.readlines():
	    print(line)

except FileNotFoundError as e:
	print("[FileNotFoundError Exception] something bad happened - {}".format(e))

except Exception as e:
	print("[inside general Exception]something bad happened - {}".format(e))

else:
	print("inside the else")

finally:
	print("inside the finally")
