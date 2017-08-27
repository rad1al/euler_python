"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# Pandigital numbers with 1,2,5,8,9 digits cannot be prime because for the case of 2,5,8,9 - the digits will sum up to a multiple of 3 making the result divisible by 3.
# Also such numbers can not end in 2,4,5,6,8 or it will be composite.
# This leaves only us with pandigital numbers with 3,4,6,7 digits to check.

from itertools import permutations
from math_tools import is_prime

pandigital = set()
pandigital.update(permutations([x for x in range(1,1+3)]))
pandigital.update(permutations([x for x in range(1,1+4)]))
pandigital.update(permutations([x for x in range(1,1+6)]))
pandigital.update(permutations([x for x in range(1,1+7)]))

def is_composite(t):
	if t[-1] == 2: return True
	if t[-1] == 4: return True
	if t[-1] == 5: return True
	if t[-1] == 6: return True
	if t[-1] == 8: return True
	return False

not_composite = filter(lambda x : not is_composite(x), pandigital)
nums = map(lambda t : int(''.join(map(str,t))), not_composite)
primes = filter(lambda x : is_prime(x), nums)

print max(primes)