from math_tools import check_palindrome

def is_lychrel(n):
	for i in xrange(50):
		s = str(n)
		v = n + int(s[::-1])
		if check_palindrome(str(v)):
			return False
		else:
			n = v
	return True

count = 0
for i in xrange(10000):
	if is_lychrel(i):
		count += 1

print count

"""
real	0m0.103s
user	0m0.066s
sys	0m0.016s
"""