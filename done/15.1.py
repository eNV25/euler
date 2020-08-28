import sys
from memoization import cached


@cached #memoization
def func(limit, x=0, y=0):
    if x >= limit or y >= limit:
        return 1
    return func(limit, x+1, y) + func(limit, x, y+1)


print(func(20))

