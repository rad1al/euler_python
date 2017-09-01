
# Brute force approach:

from math_tools import prime_factorize

found = 0
for x in xrange(1,200000):
	if len(set(prime_factorize(x))) >= 4:
		found += 1
	else:
		found = 0
	if found == 4:
		print x - 3
		break