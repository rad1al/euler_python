"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from math_tools import million_primes

primes = million_primes()
pset = set(primes)

six_consec_primes = [primes[i:i+6] for i in xrange(len(primes)-5) if sum(primes[i:i+6]) in pset]

results = list()

for k in xrange(6,1000):
	try:
		xss = [primes[i:i+k] for i in xrange(len(primes)-k+1) if sum(primes[i:i+k]) in pset]
		scan = map(sum, xss)
		max_val = max(scan)
		# print k, max_val
		results.append((k, max_val))
	except:
		pass


print results[-1]

"""
real	3m41.792s
user	3m40.456s
sys	0m0.840s
"""