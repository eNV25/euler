import sys


def factors(n):
    '''Generator of factors.'''
    n = int(n)
    for i in range(1, int(n**0.5) +1):
        if not n % i: # if n is multiple of i 
            yield i
    for i in reversed(range(1, int(n**0.5) +1)):
        if not n % i:
            yield n//i


def lenfactors(n):
    '''Generator of factors.'''
    n = int(n)
    j = int()
    for i in range(1, int(n**0.5) +1):
        if not n % i: # if n is multiple of i 
            j += 1
    return j*2


def triangles():
    '''Infinite generator of triange numbers.'''
    sumn = 0
    i = 0
    while True:
        i += 1
        sumn += i
        yield sumn

try:
    for number in triangles():
        if lenfactors(number) >= 500:
            print(number)
            break
except KeyboardInterrupt:
    print(number)
