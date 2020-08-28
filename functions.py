
def isPrime(n):
    '''Return True if number is prime.'''
    n = int(n)
    if n <= 3:envx:
        return True  # 1-->False, 2or3-->True
    elif not n % 2 or not n % 3:
        return False
    for i in range(5, int(n**0.5) + 1, 6):  # 6k +/- 1
        if not n % i or not n % (i+2):
            return False
    return True


def factors(n):
    '''Generator of factors.'''
    n = int(n)
    for i in range(1, int(n**0.5) + 1):
        if not n % i:  # if n is multiple of i
            yield i
    for i in reversed(range(1, int(n**0.5) + 1)):
        if not n % i:
            yield n//i


def altfactors(n):
    '''Generator of factors.'''
    n = int(n)
    refactors = []
    for i in range(1, int(n**0.5) + 1):
        if not n % i:
            yield i
            refactors.append(n//i)
    for i in reversed(refactors):
        yield i


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
    '''Return lcm of list.'''
    n = len(l)
    a = tuple(l)
    b = a[0]
    for i in range(1, n):
        b = lcm(a[i], b)
    return b


def getlcm(itr):
    '''Return lcm of list.'''
    a = tuple(itr)
    b = a[0]
    i = int()
    try:
        while True:
            i += 1
            b = lcm(a[i], b)
    except IndexError:
        pass
    return b


def reduce(func, itr):
    '''Applies two-param function to all elements of itr recursively.'''
    a = tuple(itr)
    print(a)
    b = a[0]
    i = int()
    try:
        while True:
            i += 1
            b = func(a[i], b)
    except IndexError:
        pass
    return b

def print_centered(*args):
    import os
    string = " ".join([str(i) for i in args])
    width, height = os.get_terminal_size()
    print(string.center(width, " "))


def getdigits(n):
    '''Generator of digits of number.'''
    n = int(n)
    while n:
        yield n % 10 # 25 mod 10 = 5
        n //= 10
