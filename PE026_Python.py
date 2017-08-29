"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from math_tools import e_sieve
from decimal import *
getcontext().prec = 3000

def detect_pattern(s):
	min_len = 5
	if len(s) < min_len:
		return False
	for i in xrange(min_len,len(s)):
		if s[i:2*i] == s[:i]:
			return s[:i]


def run():
	results = dict()
	# for i in xrange(3,1001,2):
	for i in list(e_sieve(1001)): # Only primes are really worth trying.
		pattern = detect_pattern(str(Decimal(1)/Decimal(i))[2:])
		# if pattern != None or pattern != True:
		if pattern:
			results[len(pattern)] = i
	return results

results = run()

print results[max(results.keys())]

"""
real	0m0.089s # Used to be 1.782s when using a stack in detect_pattern()
user	0m0.078s
sys	0m0.007s
"""

