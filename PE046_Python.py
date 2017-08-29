# coding: utf8
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from math_tools import squares, million_primes

sqdoubles = [x*2 for x in squares(10000)]
primes = set(million_primes())

composite_odds = {x for x in xrange(3,1000001,2)} - primes

def goldbach_candidate(n):
	for i in sqdoubles:
		if i > n:
			break
		if n - i in primes:
			return True
	return False

for n in sorted(composite_odds):
	if goldbach_candidate(n) == False:
		print n
		break

"""
real	0m0.203s
user	0m0.165s
sys	0m0.031s
"""