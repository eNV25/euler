import sys


sumn = sum(i**2 for i in range(1, 100 +1))
sqsum = sumn**2
print(sumn)
print(sqsum)
print(max(range(1, 100 +1)), min(range(1, 100 +1)))
print(sqsum - sumn)

sumjbj = int()
for i in range(1, 100 +1):
    sumjbj += i**2
print(sumjbj)