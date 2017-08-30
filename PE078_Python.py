"""
Slow method:

Have f(n,i) = number of ways we can partition n coins piles of i or less

f(n,i) = f(n-i,i) + f(n,i-1)
f(5,1) = 1
f(5,2) = f(4,2) + f(5,1) # reminds me of the coin change problem.

Putting n coints in i piles is the same as putting 1 coin in each pile and 
putting the remaining in i or fewer piles.
"""

# import numpy as np

# c = np.zeros(100000)
c = [0]*100000
c[0] = 1



for i in xrange(1,100000):
	j = 0
	while i + j < 100000:
		c[i+j] = (c[i+j] + c[j]) % 1000000
		j += 1
	if c[i] == 0:
		print i
		break

"""
With numpy:
real	37m17.796s
user	37m10.077s
sys	0m3.912s
"""