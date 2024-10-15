from implementations import *
from decimal import getcontext
import sys
import math
import time

# toda: plot error and time with respect to number

def print_fancy(*args):
    print("".join(f"{arg:<30}" for arg in args))

def get_length(number):
    if number == 0 or number == float("inf") or math.log10(number) == float("inf") :
        return 1
    return math.floor(math.log10(number)) + 1

sys.setrecursionlimit(10 ** 9)
getcontext().prec = 100000

functions = [
    iterative,
    recursive,
    memoized_recursive, 
    memoized_recursive_optimized, 
    closed,
    closed_precise,
    matrix
]

def compare_length_length(number):

    actual = iterative(number)
    actual_length_length = get_length(get_length(actual))

    print(f"actual (using iterative) length length: {actual_length_length}")

    print_fancy('function', 'error', 'length of length')

    for function in functions:
        if number > 30 and function.__name__ == 'recursive':
            print_fancy(function.__name__, 'skipped due to TOO SLOW', 'N/A')
            continue
        elif function.__name__ == 'iterative':
            print_fancy(function.__name__, 'N/A', actual_length_length)
            continue
            
        result = function(number)
        print_fancy(function.__name__, round(abs(actual - result) / actual, 20), get_length(get_length(result)))

def compare_last_10(number):
    print_fancy('function', 'error', 'last 10', 'execution time (s)')

    for function in functions:
        if number > 30 and function.__name__ == 'recursive':
            print_fancy(function.__name__, 'skipped due to TOO SLOW', 'N/A', 'N/A')
            continue
        
        # Measure the execution time
        start_time = time.time()
        result = function(number)
        if function.__name__ == 'iterative':
            actual = result
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Calculate the error and print with the execution time
        error = round(abs(actual - result) / actual, 20)
        print_fancy(function.__name__, error, int(result) % 10 ** 10, round(elapsed_time, 5))


def get_fib(number):
    print(get_length(get_length(iterative(number))))

if __name__ == '__main__':
    number = 1_000_000

    compare_last_10(number)