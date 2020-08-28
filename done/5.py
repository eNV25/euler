import sys
# check for lcm for numbers <= 20


def gcd(a, b):
    '''Return GCD of 2 numbers.'''
    a = int(a)
    b = int(b)
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    '''Returns LCM of 2 numbers.'''
    a = int(a)
    b = int(b)
    return a*b//gcd(a, b)


def getlcm(l):
    n = len(l)
    a = tuple(l)
    b = a[0]
    for i in range(1,n):
        b = lcm(a[i], b)
    return b


print(getlcm([i for i in range(1, 20 +1)])) # 1TO20
