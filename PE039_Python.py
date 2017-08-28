"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from collections import Counter

def get_pyth_triples(n):
	"""
	Generate all pythagorean triples (a,b,c) where a<b<c and c <= n.
	"""
	squares = {c**2 : c for c in range(1,n+1)}
	for a in xrange(1,n+1):
		for b in xrange(1,n+1):
			c2 = a**2 + b**2
			if c2 in squares:
				if a < b < squares[c2]:
					yield (a,b, squares[c2])

triples = list(get_pyth_triples(1000))
sums_under_1000 = filter(lambda x: x <= 1000, map(sum, triples))

count = Counter(sums_under_1000)
max_count = max(count.values())

for k in count:
	if count[k] == max_count:
		print k