"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

squares = {c**2 : c for c in range(1,1001)}

def search(squares):
	for a in xrange(1,1001):
		for b in xrange(1,1001-a):
			c2 = a**2 + b**2
			if c2 in squares:
				if a + b + squares[c2] == 1000:
					return (a, b, squares[c2])

results = search(squares)
print results[0] * results[1] * results[2]