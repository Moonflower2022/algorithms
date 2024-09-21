from implementations import *
from decimal import getcontext
import sys

# toda: plot error and time with respect to number

def print_fancy(*args):
    print("".join(f"{arg:<30}" for arg in args))

sys.setrecursionlimit(10 ** 9)
getcontext().prec = 100000

functions = [
    recursive,
    memoized_recursive, 
    memoized_recursive_optimized, 
    closed,
    closed_precise,
    iterative,
    matrix
]

number = 1000

actual = iterative(number)
actual_last_ten = actual % 10 ** 10

print(f"actual (using iterative) last 10 digits: {actual_last_ten}")

print_fancy('function', 'error', 'last 10 digits')

for function in functions:
    if number > 30 and function.__name__ == 'recursive':
        print_fancy(function.__name__, 'skipped due to TOO SLOW', 'N/A')
        continue
    elif function.__name__ == 'iterative':
        print_fancy(function.__name__, 'N/A', actual_last_ten)
        continue
        
    result = function(number)
    print_fancy(function.__name__, round(abs(actual - result) / actual, 20), result % 10 ** 10)