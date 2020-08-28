import sys


def products(n):
    '''Returns generator of products according to number of digits.'''
    n = int(n)
    for i in range(10**(n-1),10**n):
        for f in range(10**(n-1),10**n):
            yield i*f


def palindromes(n):
    '''Return generator of palindrome numbers of input iterator.'''
    for i in products(n):
        if isPal(i):
            yield i


def isPal(n):
    '''Return True if number is palindrome.'''
    x = [int(i) for i in str(n)]
    y = x.copy()
    y.reverse()
    return x == y


inp = input("number: ")
print(max(palindromes(inp)))