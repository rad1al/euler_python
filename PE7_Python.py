"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def e_sieve(n):
    multiples = set()
    for k in range(2, n+1):
        if k not in multiples:
            yield k
            multiples.update(range(k*k, n+1, k)) # update set with new elements

primes = []

for k in e_sieve(int(1e7)):
	if len(primes) == 10001:
		break
	primes.append(k)

ans = primes[-1]

print ans