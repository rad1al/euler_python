"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from math_tools import million_primes

primes = million_primes()
prime_set = set(primes)

def is_prime(n):
	if n in prime_set:
		return True
	return False

truncatable = list()

for x in primes[4:]: # the first 4 primes - 2, 3, 5, and 7 are not truncatable primes.
	num_str = str(x)
	l = len(num_str)
	left = [int(num_str[:i]) for i in range(1, l+1)]
	right = [int(num_str[-i:]) for i in range(1, l+1)]
	if len(filter(is_prime, left)) == l and len(filter(is_prime, right)) == l:
		truncatable.append(x)

ans = sum(truncatable)

print ans

"""
real	0m0.748s
user	0m0.728s
sys	0m0.015s
"""