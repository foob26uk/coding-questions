
# 1.9
# does there exist A[i] + A[j] = S, where A is sorted array, S is a target integer
def searchForPairSumsToS(A, S):
    H = {}
    for i, a in enumerate(A):
        H[S-a] = i

    for i, a in enumerate(A):
        if a in H:
            return (H[a], i)

    return -1

A = range(1,10)
print A
print range(len(A))
for i in xrange(10):
    indexes = searchForPairSumsToS(A, i)
    if indexes == -1:
        print "no sum found"
    else:
        print "A[{0}] + A[{1}] = {2}".format(indexes[0], indexes[1], i)
print
