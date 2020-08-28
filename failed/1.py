import sys

"""
in 1000
out 266333

no fucking clue wafFFts wrong
"""


def func(maxn):
    n3 = 3
    n5 = 5
    list3 = []
    list5 = []
    while True:
        list3.append(n3)
        n3 = n3 + 3
        if n3 >= maxn:
            break
    print(list3)
    while True:
        list5.append(n5)
        n5 = n5 + 5
        if n5 >= maxn:
            break
    print(list5)
    return int(sum(list3 + list5))


maxn = int(input("Maxn: "))
print(func(maxn))
