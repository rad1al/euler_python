# coding: utf8
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def pascal(lst):
	tempa = lst + [0]
	tempb = [0] + lst
	return [tempa[i] + tempb[i] for i in xrange(len(tempa))]

results = list()
row = [1]
for i in xrange(41):
	results.append(row)
	# print row[i//2]
	row = pascal(row)

print results[40][40//2]


# Noticed that the number of paths is the middle number in pascal's triangle in the (2*k)th row.
# 0x0 = 1
# 1x1 = 2
# 2x2 = 6

# 1
# 11
# 121
# 1331
# 14641


"""
real	0m0.041s
user	0m0.009s
sys	0m0.014s

"""