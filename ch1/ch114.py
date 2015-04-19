import random

#1.14

# to find the majority element in an array, just keep discarding two distinct elements and we will be left with the majority element at the end

# majority element occurs more than half the time

def findMajorityElement(arr):
	while len(arr) > 2:
		firstElement = arr.pop(0)
		i = 0
		while i < len(arr) and arr[i] == firstElement:
			i = i + 1
		if i == len(arr):
			break
		arr.pop(i)

	return arr[0]

x = range(10)
y = [5] * 10
x  = x + y
random.shuffle(x)
print x
print findMajorityElement(x)

x = range(11)
y = [9] * 10
x  = x + y
random.shuffle(x)
print x
print findMajorityElement(x)
