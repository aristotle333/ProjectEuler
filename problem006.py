'''
Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

# Finds the difference between the sum of the squares of the first n natural numbers and the square of the sum
def findDifferenceNaive(n):
    sum_of_squares = ((n*(n+1)) / 2)**2
    square_sum = 0
    for i in range(n+1):
        square_sum += (i**2)
    return sum_of_squares - square_sum

def findDifferenceEfficient(n):
    sum_of_squares = ((n*(n+1)) / 2)**2
    square_sum = (2*n+1)*(n+1)*n / 6
    return sum_of_squares - square_sum

if __name__ == "__main__":
    target = 100
    print("Naive result", findDifferenceNaive(target))
    print("Efficient result", findDifferenceEfficient(target))