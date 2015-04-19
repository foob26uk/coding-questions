import math
import random
import sys

# 1.2
def searchSortedArrayForK(sortedArr, keyK):
    lowerBound = 0
    upperBound = len(sortedArr) - 1
    while (lowerBound <= upperBound):
        middle = (upperBound - lowerBound) / 2 + lowerBound
        middleFloor = int(math.floor(middle))

        if (sortedArr[middleFloor] < keyK):
            lowerBound = middleFloor + 1
        elif (sortedArr[middleFloor] == keyK):
            if (middleFloor == 0 or sortedArr[middleFloor - 1] < keyK):
                return middleFloor
            else:
                upperBound = middleFloor - 1
        else:
            upperBound = middleFloor - 1

    return -1

if sys.argv[0] == "ch102.py":

    # check for found
    for i in xrange(10):
        index = searchSortedArrayForK(range(10), i);
        print i, index

    # check for not found
    for i in xrange(10):
        key = random.uniform(0, 10)
        index = searchSortedArrayForK(range(10), key);
        print key, index

    # check if found first occurrence (from left to right)
    arr1 = range(10);
    arr2 = range(10);
    arr = sorted(arr1 + arr2)
    print arr
    print range(10) + range(10)
    for i in xrange(10):
        index = searchSortedArrayForK(arr, i);
        print i, index
    print
