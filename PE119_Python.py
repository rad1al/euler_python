"""
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
"""

def sum_of_digits(n):
	s = 0
	while n > 0:
		s += n % 10
		n /= 10
	return s

results = []

for i in xrange(2,100):
	for j in xrange(2,10):
		v = i**j
		if sum_of_digits(v) == i:
			results.append(v)

print sorted(results)[29]

"""
real	0m0.017s
user	0m0.009s
sys	0m0.005s
"""