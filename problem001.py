'''
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000
'''

# Returns the sum of all multiples of 3 or 5 below target
def naive(target):
    sum = 0
    for i in range(1000):
        if ((i % 3 == 0) or (i % 5 == 0)):
            sum += i
    return sum

# Returns the sum of all multiples of val below target
def sumDivisibleBy(val, target):
    num_multiples = target // val
    # Use sum of consecutive integers formula: n(n+1) / 2
    return val * num_multiples * (num_multiples + 1) / 2 

def efficient(target):
    return sumDivisibleBy(3, target) + sumDivisibleBy(5, target) - sumDivisibleBy(15, target)

if __name__ == "__main__":
    target = 1000
    print("naive result:", naive(target))
    print("efficient result:", efficient(target))