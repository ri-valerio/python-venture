#!/usr/bin/python3

def main():
    # simple fibonacci series
    # the sum of two elements defines the next set
    a, b = 0, 1
    while b < 10:
        print(b, end=' ')
        b += 1

    print() # separator

    while a < 10:
        print(a, end=' ')
        a += 1
    else: # we can use else in while and for loops to perform something when it ends
    	print("done =)")



if __name__ == "__main__": main()
