"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

# fifth_powers = {str(i) : i**5 for i in xrange(10)}
fifth_powers = {'1': 1, '0': 0, '3': 243, '2': 32, '5': 3125, '4': 1024, '7': 16807, '6': 7776, '9': 59049, '8': 32768}

results = set()
for i in xrange(10, 400000): # Naive upper bound is 999,999 since 6 * 9*5 < 400,000
	if i == sum(map(lambda x : fifth_powers[x], str(i))):
		results.add(i)

print sum(results)