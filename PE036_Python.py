"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from math_tools import int2bin, check_palindrome

s = set()
for i in xrange(1,1000001):
	if check_palindrome(str(i)) and check_palindrome(int2bin(i)):
		s.add(i)

print sum(s)

"""
real	0m0.384s
user	0m0.373s
sys	0m0.007s
"""