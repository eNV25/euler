import sys
#10001th prime

try:
    inp = input("cvghjnbvc: ")
    inp = int(inp)
    pMap = [True for i in range(inp+2)]
    for i in range(2, int(inp**0.5) +1):
        if pMap[i] == True:
            for j in [i**2+x*i for x in range(inp+1)]:
                try:
                    pMap[j] = False
                except IndexError:
                    pass

    arr = [i for i in range(2,inp +1) if pMap[i] == True]

    arr2 = [f.isPrime(i) for i in arr]
    print(arr[10001])
except KeyboardInterrupt:
    arr = [i for i in range(2,inp +1) if pMap[i] == True]
    print(arr[10001])

