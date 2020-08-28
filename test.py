import sys
import os


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def getdigits(n):
    '''Generator of digits of number.'''
    n = int(n)
    while n:
        yield n % 10 # 25 mod 10 = 5
        n //= 10


print(sum(getdigits(fact(100))))
