"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from math import ceil

multiples_of_3 = {3*x for x in range(1,int(ceil(1000./3)))}
multiples_of_5 = {5*x for x in range(1,int(ceil(1000./5)))}

m_of_3_or_5 = multiples_of_3 | multiples_of_5

ans = sum(m_of_3_or_5)

print ans 