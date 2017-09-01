"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""


def power_mod(n, x, m):
	if x > 0 and x % 2 == 0:
		return power_mod(n, x/2, m) * power_mod(n, x/2, m) % m
	elif x % 2 == 1 and x > 2:
		return power_mod(n, x/2, m) * power_mod(n, x/2, m) * n % m
	elif x == 1:
		return n
	elif x == 0:
		return 1

remainders = [power_mod(x,x,10000000000) for x in xrange(1,1001)]
ans = sum(remainders) % 10000000000
print ans

"""
real	0m0.195s
user	0m0.186s
sys	0m0.004s
"""