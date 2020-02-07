import sys

def print_rec(n):
    if (n > 0):
        print_rec(n-1)
        print(f"{n}", end=" ")
        

input_val = int(sys.argv[1])
print_rec(input_val)