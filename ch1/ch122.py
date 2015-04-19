# 1.22

# given array of salaries s of employee i, and payroll target p, find cap c s.t.
# sum of salaries = p, where s_i = c if s_i > c, else s_i = s_i

def findCap(salaries, payrollTarget):
	sortedS = sorted(salaries) # O(nlogn)
	n = len(sortedS)

	print sortedS

	i = 0
	while i < len(sortedS): # O(n)
		cap = payrollTarget / float(n)
		if cap < sortedS[i]:
			return cap
		payrollTarget = payrollTarget - sortedS[i]
		n = n - 1
		i = i + 1
	return false

	# book says can use binary search instead of linear search, but not really


import random

x = []
for i in xrange(10):
	x.append(random.randint(0, 100))

c = findCap(x, 300)
print c
i = 0
while i < len(x):
	if x[i] > c:
		x[i] = c
	i = i + 1
print sorted(x)
print sum(x)