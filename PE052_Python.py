"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from math_tools import check_perm_n

for a in xrange(1,1000000):
	if check_perm_n(a,2*a):
		if check_perm_n(a,3*a):
			if check_perm_n(a,4*a):
				if check_perm_n(a,5*a):
					if check_perm_n(a,6*a):
						print a
						break

"""
real	0m0.329s
user	0m0.318s
sys	0m0.007s
"""