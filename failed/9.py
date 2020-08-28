import sys

# a < b < c
# a^2 + b^2 = c^2
# a + b + c = 1000
# find abc (product)

class BreakAll(BaseException):
    pass

inp = input("vghjb: ")
inp = int(inp)
try:
    for a in range(1,inp):
        for b in range(1,inp):
            c = int((a**2+b**2)**0.5)
            print(c)
            if a+b+c == 1000:
                raise BreakAll
except BreakAll:
    print(a*b*c)
except KeyboardInterrupt:
    print(a*b*c)
    print(a+b+c)