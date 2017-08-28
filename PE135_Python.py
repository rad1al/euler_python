"""
Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the positive integer, n, for which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?

-------------

Since x,y,z is an arithmetic progression:
x = z + 2a
y = z + a
z = z

x^2 - y^2 - z^2 = n
= (z+2a)^2 - (z+a)^2 - z^2 = n
= (z^2 + 4az + 4a^2) - (z^2 + 2az + a^2) - z^2 = n
= -z^2 + 2az + 3a^2 = n
= 3a^2 + 2az - z^2 = n
= (3a - z)(a + z) = n

Let r = 3a - z, and s = a + z,

So (3a - z)(a + z) = n
becomes r * s

r = 3(s) - 4z
4z = 3s - r
z = (3s - r)/4

s = a + z
s = -r + 4a
s = (-3a + z) + 4a
s = -r + 4a
a = (s + r)/4

z and a have to be positive integers so we can use mod 4 to check.

To make z positive, we must have 3s > r.

"""

from collections import Counter

solutions = [0] * 1000001

for r in xrange(1, 1000001):
	s = 0
	while r * s <= 1000001:
		if (r + s) % 4 == 0 and 3 * s > r and (3 * s - r) % 4 == 0:
			solutions [r * s] += 1
		s += 1

c = Counter(solutions)
print c[10]

"""
Ran in:
real	0m3.186s
user	0m3.171s
sys	0m0.010s
"""