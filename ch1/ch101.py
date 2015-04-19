import math
import random

# 1.1
def fastIntegerSquareRoot(inputInteger):
    lowerBound = 0
    upperBound = inputInteger;
    while (lowerBound <= upperBound):
        middle = (upperBound - lowerBound) / 2 + lowerBound
        middleFloor = int(math.floor(middle))
        middleCeil = middleFloor + 1 # technically this isn't the ceiling
        floorSquared = middleFloor * middleFloor
        ceilSquared = middleCeil * middleCeil

        if (floorSquared < inputInteger):
            if (ceilSquared > inputInteger):
                return middleFloor
            else:
                lowerBound = middleCeil
        elif (floorSquared == inputInteger):
            return middleFloor
        else:
            upperBound = middleFloor - 1

    return -1

for i in xrange(20):
    print i, fastIntegerSquareRoot(i)
print
