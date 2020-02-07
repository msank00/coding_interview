import cProfile
import functools
import sys

@functools.lru_cache(maxsize=None)
def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)

input_number = int(sys.argv[1])
print(fib(input_number))