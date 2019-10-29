import math

remove_mults = lambda l, n: [x for x in l if x % n != 0]

def is_prime(num):
    factors = [*range(2, math.floor(math.sqrt(num)) + 1)]
    for n in factors:
        if num % n == 0:
            return False
        else:
            factors[:] = remove_mults(factors, n)
    return True

def sieve(lim):
    primes = [*range(2, lim)]
    for n in primes:
        if not is_prime(n):
            primes[:] = remove_mults(primes, n)
    return primes
