from math_tools import million_primes
from itertools import permutations

evens = {'2','4','6','8','10'}

primes = filter(lambda x : len(x) == 4, million_primes(str))

primeset = set(primes)


def check_perm(a,b):
	if sorted(a) == sorted(b):
		return True
	else:
		return False

results = []
for i in xrange(len(primes)):
	for j in xrange(i+1, len(primes)):
		n = str(int(primes[j]) + (int(primes[j]) - int(primes[i]))) # str conversion is slow, could probably find a better way.
		if n in primeset:
			if check_perm(primes[i], primes[j]) and check_perm(primes[j],n):
				ans = primes[i] + primes[j] + n
				results.append(ans)
				break

print results[1]

"""
real	0m0.942s
user	0m0.900s
sys	0m0.022s
"""