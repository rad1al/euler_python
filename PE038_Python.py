# coding: utf8
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from math_tools import digits2int, int2digits

def concat_prod(num, xs):
	digits = list()
	for x in xs:
		digits += int2digits(num*x)
	return digits

digits = {1,2,3,4,5,6,7,8,9}

results = list()
for i in xrange(1,10000):
	for j in xrange(2,4):
		c = concat_prod(i,[x for x in xrange(1,j)])
		if len(c) == 9:
			if set(c) == digits:
				results.append(digits2int(c))

print max(results)

"""
real	0m0.094s
user	0m0.083s
sys	0m0.007s
"""