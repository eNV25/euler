import sys

# find sum of all primes under 2 million

# prime sieve
inp = input("cvghjnbvc: ")
inp = int(inp)
pMap = [True for i in range(inp+2)]
for i in range(2, int(inp**0.5) +1):
    if pMap[i] == True:
        for multiples in [i**2 + x*i for x in range(inp+1)]: # eg. if inp = 2, multiples = 4, 6, 8, 10...
            try:
                pMap[multiples] = False
            except IndexError:
                pass

# arr of primes
arr = [i for i in range(2,inp +1) if pMap[i] == True]
print(sum(arr))