import sys


def isSunday(start):
    '''Will yield True if day is Sunday. 
    
    Argument start is integer corresponding
    to initial day of week. 
    (ie. 1 for Monday, 7 for Sunday)

    If start is 1 (Monday), 
    will yield False 6 times, 
    then True (for Sunday).
    '''
    n = 7 - start 
    for i in range(n): # 
        yield False
    yield True
    while True:
        for i in range(6):
            yield False
        yield True


def dayGenerator():
    '''
    Generates years (from 01/01/1901 to 31/12/2000) in the format:
    
    (day, month, year)
    '''
    for year in range(1901, 2000 +1):
        for day in range(1, 31 +1):     yield day,  1, year # Jan
        if (not year % 4 and not year % 100 and year % 400): # noleap
            for day in range(1, 28 +1): yield day,  2, year # Feb
        elif year % 4: # noleap
            for day in range(1, 28 +1): yield day,  2, year
        elif not year % 4 or (not year % 4 and not year % 100 and not year % 400):# leap
            for day in range(1, 29 +1): yield day,  2, year # 
        for day in range(1, 31 +1):     yield day,  3, year # Mar
        for day in range(1, 30 +1):     yield day,  4, year # Apr
        for day in range(1, 31 +1):     yield day,  5, year # May
        for day in range(1, 30 +1):     yield day,  6, year # Jun
        for day in range(1, 31 +1):     yield day,  7, year # Jul
        for day in range(1, 31 +1):     yield day,  8, year # Aug
        for day in range(1, 30 +1):     yield day,  9, year # Sep
        for day in range(1, 31 +1):     yield day, 10, year # Oct
        for day in range(1, 30 +1):     yield day, 11, year # Nov
        for day in range(1, 31 +1):     yield day, 12, year # Dec

count = int()
i = int()
for (day, month, year), sunday in zip(dayGenerator(), isSunday(2)):
    if not month == 1: continue
    if sunday: count += 1; print(day, month, year)
    # print(day, month, year, sunday)
    # if sunday: break
print(count, i)
