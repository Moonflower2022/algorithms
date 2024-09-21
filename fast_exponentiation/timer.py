from implementations import fast_pow
from numpy import power
from math import pow
import timeit

def base_pow(a, b):
    return a ** b

def evaluate(exp_funciton, base, exponent, iterations):
    total_time = timeit.timeit(lambda: exp_funciton(base, exponent), number=iterations)
    return total_time


if __name__ == '__main__':
    functions = [
        fast_pow,
        power,
        pow,
        base_pow
    ]

    base = 123
    exponent = 6
    iterations = 4000000

    for function in functions:
        print(f"{function.__name__}: {evaluate(function, base, exponent, iterations)}")