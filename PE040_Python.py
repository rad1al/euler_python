# coding: utf8
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from math_tools import product

digits = [str(i) for i in xrange(1,200000)]
pattern = '.' + ''.join(digits)

dns = map(int, (pattern[1], pattern[10], pattern[100], pattern[1000], pattern[10000], pattern[100000], pattern[1000000]))
# print dns 
print product(dns)
