'''
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from math import sqrt, floor, log

def lcm_of_all_integers_until(n):
    limit = sqrt(n)
    primes = getPrimes(n)
    check = True
    N = 1
    for p in primes:
        a = 1
        if check:
            if p <= limit:
                a = floor(log(n) / log(p))
            else:
                check = False
        N = N * p ** a
    return N

# Retruns a list of primes until n
def getPrimes(n):
    primes = []
    for p in range(2, n+1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            primes.append(p)
    return primes

if __name__ == "__main__":
    target = 20
    print(lcm_of_all_integers_until(target))