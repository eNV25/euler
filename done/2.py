import sys

def fibonacci(maxn):
    maxn = int(maxn)
    n1 = 1
    n2 = 2
    nn = 1
    fibo = [1, 2]
    while True:
        n3 = n1 + n2
        fibo.append(n3)
        nn = nn + 1
        n1 = n2 
        n2 = n3
        if fibo[nn] >= maxn:
            break
    return fibo

fibo = fibonacci(input("maxn: "))
evenfibo = []
for i in fibo:
    if not i % 2:
        evenfibo.append(i)
print(sum(evenfibo))

"""
in 4000000
out 4613732
"""