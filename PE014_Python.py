# Memoized implementation

lookup = dict()

def collatz(path):
	last = path[-1]
	if last == 1:
		lookup[path[0]] = path
		return path
	if last % 2 == 0:
		nxt = last / 2
	else:
		nxt = 3 * last + 1
	if nxt in lookup:
		return collatz(path + lookup[nxt])
	else:
		path.append(nxt)
	return collatz(path)

def f(n):
	max_chain = [1]
	for i in xrange(1,1000001):
		chain = collatz([i])
		if len(chain) > len(max_chain):
			max_chain = chain
	return max_chain[0]

print f(1000000)

"""
real	0m11.066s
user	0m10.281s
sys	0m0.765s
"""

# -------- Old implementation -------------

# from math_tools import get_k_with_largest_v

# def collatz(n):
# 	if n == 1:
# 		return n
# 	elif n % 2 == 0:
# 		return n / 2
# 	elif n % 2 == 1:
# 		return 3*n + 1

# # lookup = dict()

# results = dict()
# for i in xrange(1,1000001):
# 	chain = 1
# 	n = i
# 	while True:
# 		chain += 1
# 		n = collatz(n)
# 		if n == 1:
# 			break
# 	results[i] = chain


# print get_k_with_largest_v(results)

# """
# real	0m38.790s
# user	0m38.508s
# sys	0m0.182s
# """


