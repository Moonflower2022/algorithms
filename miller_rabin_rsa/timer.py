import time
import pandas as pd
from old_primality import is_prime
from miller_rabin import is_prime_miller_rabin

if __name__ == "__main__":
    numbers = range(199_999_999_999_000, 200_000_000_000_000)
    s = 20

    start = time.time()
    miller_rabin_tested = [is_prime_miller_rabin(i, s) for i in numbers]
    print("Miller Rabin Running Time (s):", time.time() - start)

    start = time.time()
    normal_tested = [is_prime(i) for i in numbers]
    print("Normal Running Time (s):", time.time() - start)

    # Create a DataFrame from the arrays

    if normal_tested == miller_rabin_tested:
        print("Tests return the same result!")
    else: 
        df = pd.DataFrame({'i': [i for i in numbers], 'normal_test': normal_tested, 'miller_rabin_test': miller_rabin_tested})
        print(df)
        print("Tests did not return the same result!")
