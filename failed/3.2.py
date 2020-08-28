import sys

# 6k +/- 1

def getPrimeFactors(n):
    m = int(n)
    while not m % 2:
        yield 2
        m //= 2 
    while not m % 3:
        yield 3
        m //= 3
    for i in range(5, n, 6):
        while not m%i:
            yield i
            m //= i
        while not m%(i+2):
            yield i+2
            m //= i+2


inp = input("dgbbv: ")
inp = int(inp)
# for i in getPrimeFactors(inp):
#     print(i)
#     print(f.isPrime(i))
print(max(getPrimeFactors(inp)))

