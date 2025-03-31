import random
from miller_rabin import is_prime_miller_rabin

def generate_prime(min, max): # if there are no primes between min and max (inclusive) then the function just freezes
    number = random.randint(min, max)
    while not is_prime_miller_rabin(number):
        number = random.randint(min, max)
    return number

if __name__ == '__main__':
    print(generate_prime(2 ** 255, 2 ** 256))