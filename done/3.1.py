import sys
# get primefactors
# primetest filter method
# performance is bad if prime factor is big


def factors(n):
    '''Generator of factors.'''
    n = int(n)
    for i in range(1, int(n**0.5) +1):
        if not n % i: # if n is multiple of i 
            yield i
    for i in reversed(range(1, int(n**0.5) +1)):
        if not n % i:
            yield n//i


def altfactors(n):
    '''Generator of factors.'''
    n = int(n)
    refactors = []
    for i in range(1, int(n**0.5) +1):
        if not n % i:
            yield i
            refactors.append(n//i)
    for i in reversed(refactors):
        yield i


def getPrimeFactors(n):
    '''Generator of prime factors.'''
    n = int(n)
    for i in factors(n):
        if isPrime(i):
            yield i


def isPrime(n):
    '''Return True if number is prime.'''
    n = int(n)
    if n <= 3:
        return True # 1-->False, 2or3-->True
    elif not n%2 or not n%3:
        return False
    for i in range(5, int(n**0.5) +1, 6): # 6k +/- 1
        if not n%i or not n%(i+2):
            return False
    return True


inp = input("nbr: ")
print(max(getPrimeFactors(inp)))

