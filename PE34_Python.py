"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def fac(n):
	if n <= 1:
		return 1
	else:
		return n * fac(n-1)

fac_dict = {x : fac(x) for x in range(10)}

def digit_fac_sum(n):
	return sum([fac_dict[int(x)] for x in str(n)])

def run():
	results = list()
	for i in xrange(3,100000):
		if i == digit_fac_sum(i):
			results.append(i)
	return results

results = run()
print sum(results)