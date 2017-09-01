from itertools import permutations

digits = [1,2,3,4,5,6,7,8,9,0]

def digits2int(ds):
	n = 0
	k = 1
	i = len(ds) - 1 # Allows it to work for tuples too, whereas 
	while i >= 0:	# original approach with pop() only worked with lists.
		n += k*ds[i]
		k *= 10
		i -= 1
	return n

def check_substr_divis(p):
	if p[3] % 2 != 0:
		return False
	if sum(p[2:5]) % 3 != 0:
		return False
	if p[5] % 5 != 0:
		return False
	if digits2int(p[4:7]) % 7 != 0:
		return False
	if (p[5] - p[6] + p[7]) % 11 != 0:
		return False
	if digits2int(p[6:9]) % 13 != 0:
		return False
	if digits2int(p[7:10]) % 17 != 0:
		return False
	return True

check_substr_divis([1,4,0,6,3,5,7,2,8,9]) == True

total = 0
for p in permutations(digits):
	if check_substr_divis(p):
		total += digits2int(p)

print total

"""
real	0m1.226s
user	0m1.218s
sys	0m0.005s
"""