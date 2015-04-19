from ch102 import searchSortedArrayForK

# 1.7
# sorted arrays A and B, length n and m respectively
# return A intersect B
# (1) n ~ m <- linear search through both arrays
# (2) n << m <- for each element in n, do binary search on m

def intersectionV1(A, B):
    intersection = []
    indexA = 0
    indexB = 0
    lengthA = len(A)
    lengthB = len(B)
    while indexA < lengthA and indexB < lengthB:
        if A[indexA] == B[indexB]:
            element = A[indexA]
            intersection.append(element)
            while A[indexA] == element:
                indexA = indexA + 1
                if (indexA == lengthA):
                    break
            while B[indexB] == element:
                indexB = indexB + 1
                if (indexB == lengthB):
                    break
        elif A[indexA] < B[indexB]:
            indexA = indexA + 1
        elif A[indexA] > B[indexB]:
            indexB = indexB + 1

    return intersection
                                
A = [-1, 2, 3, 3, 4, 5, 100]
B = range(10)
print A
print B
print intersectionV1(A,B)
print

def intersectionV2(A, B):
    smallArr = A if len(A) < len(B) else B
    largeArr = A if len(A) > len(B) else B
    intersection, lastElement = [], None

    for element in smallArr:
        if (element != lastElement):
            index = searchSortedArrayForK(B, element)
            if (index != -1):
                intersection.append(element)
        lastElement = element

    return intersection

A = [-1, 2, 3, 3, 4, 5, 100]
B = range(50)
print A
print B
print intersectionV2(A,B)
print
