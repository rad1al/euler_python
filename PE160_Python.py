# Work in progress

def rmvtrailing(n):
	"""Remove trailing zeroes"""
	while n % 10 == 0:
		n = n / 10
	return n

def func(s,n):
	total = 1
	found5 = 0
	for i in xrange(s,n+1):
		total = rmvtrailing(total)
		j = rmvtrailing(i)
		# print j
		if found5 > 0:
			k = j
			while k % 2 == 0 and found5 > 0:
				k = k / 2
				found5 -= 1
			# total *= k % 100000
			total *= k
			
		# elif j % 5 == 0 and j % 2 == 1:
		elif j % 5 == 0:
			k = j
			while k % 5 == 0:
				k = k / 5
				found5 += 1
			# total *= k % 100000
			total *= k
		# elif i % 10 == 0:
		# 	k = i
		# 	while k % 10 == 0 and k > 9:
		# 		k = k / 10
		# 	total *= k % 100000	
		else:
			# total *= j % 100000
			total *= j
		# print total
		total = total % 100000
	return total % 100000

# print func(1,10**9)
# print func(1,10**6) * func(1,10**6) % 100000
# print func(1,10**3)
# print func(1,9)
# print func(100001,200000)

"""
Timings for func(1,n) where n =:
10^4 : real	0m0.049s
10^5 : 0m0.061s
10^6 : 0m0.451s
10^7 : 0m4.382s
10^8 : 0m45.526s
10^12 expected time: 450000 seconds or 125 hours.
"""

























