def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        dec=str(i)
        oct_=oct(i)[2:]
        hex_=hex(i)[2:].upper()
        bin_=bin(i)[2:]
        print(dec.rjust(width), oct_.rjust(width), hex_.rjust(width), bin_.rjust(width)) 
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)