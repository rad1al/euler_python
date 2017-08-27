# coding: utf8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from math_tools import check_palindrome

def find_all_multiples_of_3_digit_nums():
	prime_multiples = map(lambda x: int(x), filter(check_palindrome, {str(a*b) for a in range(100,1000) for b in range(100, 1000)}))
	return prime_multiples

pali_set = find_all_multiples_of_3_digit_nums()

ans = max(pali_set)

print ans