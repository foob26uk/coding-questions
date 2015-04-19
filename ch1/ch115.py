# 1.15

# array with n elements, use O(k) memory to identify all elements that occur more than ceil(n/k) times, can read array twice

import random
import copy
import math

def findCommonWords(arr, k):
	arr2 = copy.copy(arr)
	# keep discarding k distinct elements (one pass over array)
	while len(arr) > k:
		map = {}
		i = 0
		numberDiscarded = 0
		while numberDiscarded < k:
			while i < len(arr) and arr[i] in map:
				i = i + 1
			if i == len(arr):
				break
			map[arr.pop(i)] = 0
			numberDiscarded = numberDiscarded + 1

		if i == len(arr):
			break

	# arr is now a super set of answer, need to count number of occurrences
	for x in arr2:
		if x in map:
			map[x] = map[x] + 1
	result = []
	for x in map:
		if map[x] > math.ceil(len(arr2) / k):
			result.append(x)
	return result

x = range(11)
y = [9] * 10
x  = x + y
random.shuffle(x)
print x
print findCommonWords(x, 2)

x = range(10) + [10] * 11 + [11] * 11
random.shuffle(x)
print x
print findCommonWords(x, 3)

x = [1] * 10 + [2] * 11 + [3] * 11
random.shuffle(x)
print x
print findCommonWords(x, 3)

x = [1] * 3 + [2] * 3 + [3] * 3
random.shuffle(x)
print x
print findCommonWords(x, 2)
