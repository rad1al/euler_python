"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def spiral(n):
	total = 0
	x = 1
	count = 0
	inc = 2
	limit = n**2
	while True:
		if x > limit:
			break
		# print x
		total += x
		x += inc
		count += 1
		if count == 4:
			count = 0
			inc += 2
	print total

spiral(1001)

"""
real	0m0.016s
user	0m0.009s
sys	0m0.005s
"""

# def spiral(n):
# 	lst = [x for x in xrange(1,n**2+1)]
# 	# lst = [x for x in xrange(1,26)]
# 	nums = list()
# 	x = 0
# 	count = 0
# 	inc = 2
# 	limit = n**2
# 	while True:
# 		if x > limit:
# 			break
# 		nums.append(lst[x])
# 		x += inc
# 		count += 1
# 		if count == 4:
# 			count = 0
# 			inc += 2
# 	print sum(nums)

# spiral(1001)

"""
real	0m0.073s
user	0m0.049s
sys	0m0.021s
"""