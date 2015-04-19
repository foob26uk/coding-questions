# 1.20

# given set of lines (a_i, b_i) for i = 0,1,...,n-1, return pair of lines s.t.
# one line is completely contained inside the other line

def findContainedInterval(lines):
	# sort the input, then traverse once, check if neighbor contains
	# O(nlogn)
	sortedLines = sorted(lines, key=lambda line: line[0])

	print sortedLines

	i = 1
	while i < len(sortedLines):
		if sortedLines[i][1] <= sortedLines[i-1][1]:
			return (sortedLines[i], sortedLines[i-1])
		i = i + 1

import random

x = []
for i in xrange(10):
	y = random.randint(0, 10)
	x.append((y, random.randint(1,10) + y))

random.shuffle(x)
print findContainedInterval(x)