'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# Returns the largest prime factor of n
def largestPrimeFactor(n):
    factors = set()
    d = 2
    while n > 1:
        while n % d == 0:
            factors.add(d)
            n /= d

        # Increase d by 2 if it is not equal to 2 (no need to check even numbers for prime factors)
        if d != 2:
            d += 2
        else:
            d += 1
        if d*d > n:
            if n > 1: 
                factors.add(n)
            break

    largest_prime_factor = max(factors)
    return largest_prime_factor

if __name__ == "__main__":
    target = 600851475143
    print(largestPrimeFactor(target))