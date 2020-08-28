import sys


def chain(n):
    i = 1
    while n != 1:
        i += 1
        if n%2:
            n = 3*n+1
        else:
            n = n//2
    return i

arr = []
for i in range(1,1000000):
    arr += [chain(i)]
print(arr.index(max(arr)) +1)
