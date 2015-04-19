import math
import random

# 1.5
def searchSortedArrayOfUnknownLength(sortedArr, keyK):
    i = 0
    while (True):
        try:
            index = (1 << i) - 1 # bitwise left shift
            val = sortedArr[index]
            if (val == keyK):
                return index
            elif (val > keyK): # keyK is less than it, need to search and find it
                break
            # if val < keyK, just keep looping
        except IndexError:
            break
        i = i + 1

    # search between 2^(i - 1) and 2^i - 1
    lowerBound = 1 << (i - 1)
    upperBound = (1 << i) - 1

    while (lowerBound <= upperBound):
        middle = (upperBound - lowerBound) / 2 + lowerBound
        middleFloor = int(math.floor(middle))

        try:
            val = sortedArr[middleFloor]
            if (val == keyK):
                return middleFloor
            elif (val < keyK):
                lowerBound = middleFloor + 1
            else: # val > keyK
                upperBound = middleFloor - 1
        except IndexError:
            upperBound = middleFloor - 1
        
    return -1

arr = range(10)
for i in xrange(10):
    print i, searchSortedArrayOfUnknownLength(arr, i)
print 10, searchSortedArrayOfUnknownLength(arr, 10)
print
