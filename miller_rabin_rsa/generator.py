import random
from miller_rabin import miller_rabin

def generate_prime(min, max, s): # if there are no primes between min and max (inclusive) then the function just freezes
    ret = random.randint(min, max)
    while not miller_rabin(ret, s):
        ret = random.randint(min, max)
    return ret

if __name__ == '__main__':
    print(generate_prime(2 ** 255, 2 ** 256, 20))