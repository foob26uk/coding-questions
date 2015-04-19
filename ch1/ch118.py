# given two sorted arrays, length m and n
# give O(log m + log n) time algo for computing k-th smallest element of array union
# elements may be repeated

# wrote code that only worked if k < size of each array
# then copied the answer from the back of book, which doesn't work most of time....

import random
import math

def findKthElement(arr1, arr2, k):
	lower = 0
	upper = k

	lower = max(0, k - len(arr2))
	upper = min(len(arr1), k)

	# find el s.t. lower <= el < upper s.t. arr1[0]..arr1[el - 1] and
	#   arr2[0]..arr2[k-el-1] are the smallest k numbers
	while lower < upper:
		el = int(math.floor((upper - lower) / 2 + lower))

		if el < len(arr1) and k - 1 > 0 and arr2[k - el - 1] > arr1[el]:
			lower = el + 1
		elif el > 0 and k - 1 < len(arr2) and arr1[el - 1] > arr2[k - el]:
			upper = el
		else:
			lower = el
			break

	if lower == 0:
		return arr2[k - 1]
	elif lower == k:
		return arr1[k - 1]
	else:
		return max(arr1[lower - 1], arr2[k - lower - 1])


for i in xrange(10):
	arr1 = []
	arr2 = []
	for x in xrange(10):
		arr1.append(random.randint(0, 100))
		arr2.append(random.randint(0, 100))

	arr1.sort()
	arr2.sort()
	arr = arr1 + arr2
	arr.sort()
	print arr1
	print arr2
	print arr
	k = random.randint(1,len(arr))
	result = findKthElement(arr1, arr2, k)
	print arr[k - 1], result
	if arr[k - 1] != result:
		print "error"
		break


