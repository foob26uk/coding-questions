import random

#1.13
# find the largest ordered difference d, lowest height before highest height, and the minimum battery capacity is mgd

# O(n)

def findMinimumBatteryCapacity(arr):
	result = 0
	min = 0
	for i in range(1, len(arr)):
		if arr[i] - min > result:
			result = arr[i] - min
		if arr[i] < min:
			min = arr[i]

	return result

arr = []
for i in range(10):
	arr.append(random.randint(-10,10))
print arr
print findMinimumBatteryCapacity(arr)