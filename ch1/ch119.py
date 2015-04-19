# 1.19

# determine if a given set of straight lines intersect in a given rectangle

def linesIntersect(lines):
	# assume lines in rectangle are defined by two points, first point on left edge,
	# second point on right edge

	# no intersection if for any pair of points, they are either both bigger or smaller
	# than any other pair of points
	sortedLines = sorted(lines, key=lambda line: line[0])

	i = 1
	while i < len(sortedLines):
		if sortedLines[i][1] < sortedLines[i - 1][1]:
			return True
		i = i + 1
	return False


import random
x = []
for i in xrange(10):
	x.append((i, i))
print x
print linesIntersect(x)
random.shuffle(x)
print linesIntersect(x)

x[random.randint(0, 10)] = (5, 10)
print linesIntersect(x)