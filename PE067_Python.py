"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
"""

from io_tools import read_data

data = read_data("data/PE67_triangle.txt")
s = [row.split() for row in data]
s = [map(int,row) for row in s]

def merge(lst1, lst2):
	if len(lst1) == 1:
		return lst1[0]
	return [max(lst1[i] + lst2[i], lst1[i+1] + lst2[i]) for i in xrange(len(lst2))]

collapsed = reduce(lambda rowb,rowa : merge(rowb, rowa),reversed(s))
print collapsed[0]

"""
real	0m0.021s
user	0m0.012s
sys	0m0.005s
"""