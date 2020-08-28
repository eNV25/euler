import sys

def getdigits(n):
    '''Generator of digits of number.'''
    n = int(n)
    while n:
        yield n % 10 # 25 mod 10 = 5
        n //= 10


x = 2**1000
print(sum(getdigits(x)))
