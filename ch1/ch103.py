
import math
import random

# 1.3
def searchSortedArrayForFirstLarger(sortedArr, keyK):
    lowerBound = 0
    upperBound = len(sortedArr) - 1
    while (lowerBound <= upperBound):
        middle = (upperBound - lowerBound) / 2 + lowerBound
        middleFloor = int(math.floor(middle))

        if (sortedArr[middleFloor] <= keyK):
            lowerBound = middleFloor + 1
        else: # > keyK
            if (sortedArr[middleFloor - 1] <= keyK):
                return middleFloor
            else:
                upperBound = middleFloor - 1

    return -1

arr1 = range(10);
arr2 = range(10);
arr = sorted(arr1 + arr2)
print arr
print range(10) + range(10)
for i in xrange(10):
    index = searchSortedArrayForFirstLarger(arr, i)
    print i, index
print
