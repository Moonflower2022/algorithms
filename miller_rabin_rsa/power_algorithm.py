import time

def power_modulus(x, y, p): # returns x^y % p
    residue = 1
    x = x % p # Take modulo of x if it's larger than p
    while y > 0:
        if y & 1:
            residue = (residue * x) % p
        y = y >> 1
        x = (x * x) % p
    return residue

if __name__ == '__main__':
    start_time = time.time()
    [power_modulus(i, i, 10) for i in range(20, 3000)]
    our_time = time.time() - start_time
    start_time = time.time()
    [(i ** i) % 10 for i in range(20, 3000)]
    their_time = time.time() - start_time

    print("our running time (s):", our_time)
    print("unoptimized running time (s)", their_time)