"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


results = list()
for n in xrange(1,1000):
	for k in xrange(1,1000):
		v = n**k
		if len(str(v)) == k:
			results.append((n,k))
		if len(str(v)) > k:
			break

print len(results)

"""
real	0m0.076s
user	0m0.064s
sys	0m0.008s
"""