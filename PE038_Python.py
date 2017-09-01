from math_tools import digits2int, int2digits

def concat_prod(num, xs):
	digits = list()
	for x in xs:
		digits += int2digits(num*x)
	return digits


results = list()
for i in xrange(1,1000):
	for j in xrange(2,10):
		c = concat_prod(i,[x for x in xrange(1,j)])
		if len(c) == 9:
			if len(set(c)) == 9:
				print i, [x for x in xrange(1,j)
				results.append(digits2int(c))

print max(results)