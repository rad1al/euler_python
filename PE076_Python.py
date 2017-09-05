"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

# Adaptation of Dynamic Programming solution for problem #31

target = 100
ways = [0] * (target+1)
ways[0] = 1

for i in xrange(1,target):
	for j in xrange(i, target+1):
		ways[j] += ways[j-i]

print ways[-1]
# print ways

"""
for target = 11:
[1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 41]

real	0m0.017s
user	0m0.010s
sys	0m0.005s
"""