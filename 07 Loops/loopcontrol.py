#!/usr/bin/python3

def main():
	s = 'thisx isx ax string!x motherfucker!'
	for c in s:
		if c == 'x': continue
		if c == 'm': break
		print(c, end='')


	print() # separator


	for c in "bazinga":
			print(c, end='')
	else:
		print(" - done =)")


if __name__ == "__main__": main()
