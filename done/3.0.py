import sys
# get prime factors
# multiples sieve method


def factors(n):
    '''Generator of factors.'''
    n = int(n)
    for i in range(1, int(n**0.5) +1):
        if not n % i: # if n is multiple of i 
            yield i
    for i in reversed(range(1, int(n**0.5) +1)):
        if not n % i:
            yield n//i

def sieve(factors):
    '''Returns primefactorlist if input is factorlist.'''
    factors = list(factors)
    copy1 = factors.copy()  # cuz python wierdness
    copy1.remove(1)  # everything is divisible by 1, so result would always 1
    for i in copy1:
        copy2 = factors.copy()
        try:
            copy2.remove(i)
        except ValueError: # raised when value has already been removed
            pass
        for f in copy2:
            if not f % i:  # if f is multiple of i then remove f
                try:
                    factors.remove(f)
                except ValueError:
                    # raised if f has already been removed, so to offset lenl--:
                    pass
    return factors 

def getPrimeFactors(n):
    '''Return primefactorlist of input.'''
    return sieve(factors(n))

inp = input("qkjfbwkv: ")
print(max(getPrimeFactors(inp)))


def primef(num): # old
    # get ordered factorlist
    factors = []
    refactors = []
    lenfactors = 0
    num = int(num)
    for i in range(1, int(num**0.5) + 1):  # range of sqrt of num
        if not num % i:
            refactors.append(num//i)
            factors.append(i)
    factors += reversed(refactors)
    # print(factors)

    # get ordered primefactorlist
    copy1 = factors.copy()  # cuz python wierdness
    copy1.remove(1)  # everything is divisible by 1, so result would always 1
    for i in copy1:
        copy2 = factors.copy()
        try:
            copy2.remove(i)
        except ValueError: # raised when value has already been removed
            pass
        for f in copy2:
            if not f % i:  # if f is multiple of i then remove f
                try:
                    factors.remove(f)
                except ValueError:
                    # raised if f has already been removed, so to offset lenfactors--:
                    pass
    # print(factors)

    # get largest at the end
    return factors


# inp = input("enter number: ")
# print(max(primef(inp)))
