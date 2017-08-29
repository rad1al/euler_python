"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math_tools import is_prime

primes = [2]

for x in range(3, int(2e6), 2):
	if is_prime(x) == True:
		primes.append(x)

ans = sum(primes)

print ans