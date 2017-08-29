# coding: utf8
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""



def run():
	results = dict()
	for a in xrange(100,2001):
		for b in xrange(1,101):
			s = str(a) + str(b) + str(a*b)
			if len(s) > 9:
				continue
			v = {x for x in s}
			if len(v) == 9 and '0' not in v:
				results[a*b] = (a,b)
	return results

results = run()
print sum(results.keys())

"""
real	0m0.123s
user	0m0.114s
sys	0m0.005s
"""

# --------- Slower method:

# from itertools import permutations

# digits = [1,2,3,4,5,6,7,8,9]

# def digits2num(ds):
# 	s = ''.join(map(str,ds))
# 	return int(s)

# products = set()

# for arrangement in permutations(digits):
# 	for i in xrange(1,8):
# 		for j in xrange(i+1,9):
# 			x = arrangement[:i]
# 			y = arrangement[i:j]
# 			z = arrangement[j:]
# 			xnum = digits2num(x)
# 			ynum = digits2num(y)
# 			znum = digits2num(z)
# 			if xnum*ynum == znum:
# 				products.add(znum)
			
# print sum(products)

# """
# real	0m39.175s
# user	0m39.141s
# sys	0m0.018s
# """
