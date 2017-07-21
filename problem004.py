'''
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# Returns the largest palindrome from the product of 3-digit numbers
def largestPalindrome():
    largestPalindrome = 0
    a = 999
    while a >= 100:
        b = 999
        while b >= a:
            if a*b <= largestPalindrome:
                break
            if isPalindrome(a*b):
                largestPalindrome = a*b
            b -= 1
        a -= 1
    return largestPalindrome

def isPalindrome(val):
    return str(val) == str(val)[::-1]

if __name__ == "__main__":
    print(largestPalindrome())