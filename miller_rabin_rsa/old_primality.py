from math import isqrt

def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

if __name__ == '__main__':
    '''
    import time

    numbers = range(19999999999000, 20000000000000)

    start = time.time()
    normal_tested = [is_prime(i) for i in numbers]
    print("Normal Running Time (s):", time.time() - start)
    '''

    number = 1688969029158268024624655682727
    print(f"is_prime({number}): {is_prime(number)}")