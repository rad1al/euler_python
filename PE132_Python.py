from math_tools import million_primes
primes = million_primes()

def factor_repunit(n):
	# rep(n) = (10^n - 1)/9
	# (10^n - 1)/9 congr. 0 mod p
	# (10^n - 1) congr. 0 mod 9*p
	# (10^n) congr. 1 mod 9*p
	factors = list()
	b = n
	i = 0
	count = 0
	while count < 40:
		if pow(10,b,9*primes[i]) == 1:
			factors.append(primes[i])
			count += 1
		i += 1
	return factors

factors = factor_repunit(10**9)
print sum(factors)


"""
real	0m0.092s
user	0m0.077s
sys	0m0.012s
"""


def trailing(n):
	lst = [x if x % 5 != 0 else  for x in range(1,n+1)]
	for 
	return lst

def trailing(n):
	nums = list()
	for i in xrange(1,n+1):
		if i % 5 == 0
			k = i
			while k % 5 == 0:
				k /= 5

			nums.append(i)
		if i % 10 
		nums.append(i)
	return nums

def stupid(n):
	n = reduce(lambda x,y : (x*y), [k for k in range(9)])

def number_of_zeros(n):
	lst = [1 for x in xrange(1,(n/5)+1)]
	k = 5
	while k <= len(lst):
		for i in xrange(k-1, len(lst), k):
			lst[i] += 1
		k *= 5
	return lst

def func(n):
	total = 1
	found5 = False
	for i in xrange(n)
		if found5:
			total = i / 2
		if i % 5 == 0 and i % 2 == 1:
			found5 = True














