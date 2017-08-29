# coding: utf8
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math_tools import factorize

def proper_factors(n):
	return factorize(n) - {n}

vals = list()
for x in xrange(10000):
	sum_of_proper_factors = sum(proper_factors(x))
	if sum_of_proper_factors != x and sum(proper_factors(sum_of_proper_factors)) == x:
		vals.append(x)

ans = sum(vals)

print ans

"""
real	0m0.139s
user	0m0.128s
sys	0m0.006s
"""