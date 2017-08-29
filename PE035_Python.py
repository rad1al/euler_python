from itertools import permutations, combinations
from math_tools import million_primes

primes = million_primes()
prime_set = set(primes)

def is_prime(n):
	if n in prime_set:
		return True
	return False

def rotations(s):
	return [s[-i:] + s[:-i] for i in range(len(s))]

def digit_filter(n): # to filter numbers with a 0,2,4,5,6, or 8 in its digits.
	s = str(n)
	if ('0' in s) or ('2' in s) or ('4' in s) or ('5' in s) or ('6' in s) or ('8' in s):
		return False
	return True

def convert_digits_to_num(digits):
    return int(''.join(digits))

results = {2,3,5}

candidate_primes = filter(digit_filter, primes[3:])

for x in candidate_primes:
	if all(map(is_prime, map(convert_digits_to_num, rotations(str(x))))):
		results.add(x)

ans = len(results)

print ans