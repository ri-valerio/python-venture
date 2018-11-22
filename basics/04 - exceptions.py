
try:
	fh = open('xlines.txt')
	for line in fh.readlines():
	    print(line)

# speficif error
except FileNotFoundError as e:
	print("[FileNotFoundError Exception] something bad happened - {}".format(e))

#general error
except Exception as e:
	print("[inside general Exception]something bad happened - {}".format(e))

else:
	print("This is going to print if everything goes OK")

finally:
	print("This is going to print no matter what")
