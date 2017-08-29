"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

from math_tools import get_digits

nums = [x**y for x in range(90, 100) for y in range(90, 100)]

digit_sums = map(sum, map(lambda x : map(int, get_digits(x)), nums))

ans = max(digit_sums)

print ans

"""
real	0m0.026s
user	0m0.017s
sys	0m0.006s
"""