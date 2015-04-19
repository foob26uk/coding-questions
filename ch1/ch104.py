import math
import random

# 1.4
def searchSortedArrayForAIEqualsI(sortedArr):
    lowerBound = 0
    upperBound = len(sortedArr) - 1
    while (lowerBound <= upperBound):
        middle = (upperBound - lowerBound) / 2 + lowerBound
        middleFloor = int(math.floor(middle))

        if (sortedArr[middleFloor] < middleFloor):
            lowerBound = middleFloor + 1
        elif (sortedArr[middleFloor] == middleFloor):
            return middleFloor
        else: # > middleFloor
            upperBound = middleFloor - 1

    return -1

arr = [-1, 0, 2, 4, 7]
print searchSortedArrayForAIEqualsI(arr)
arr = [-1, 0, 1, 2, 3]
print searchSortedArrayForAIEqualsI(arr)
arr = [-1, 0, 1, 2, 4]
print searchSortedArrayForAIEqualsI(arr)
print
