# coding: utf8
"""
The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

    Unsorted       Sorted
    n  rad(n)   n  rad(n) k
    1    1      1    1    1
    2    2      2    2    2
    3    3      4    2    3
    4    2      8    2    4
    5    5      3    3    5
    6    6      9    3    6
    7    7      5    5    7
    8    2      6    6    8
    9    3      7    7    9
    10   10     10   10   10

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""

from math_tools import prime_factorize, product
from operator import itemgetter

rads = [(1,1)] + [(x, product(set(prime_factorize(x)))) for x in range(2,100001)]

sorted_rads = sorted(rads, key=itemgetter(1,0))

print sorted_rads[9999][0]

"""
Runs in:
real    1m13.928s
user    1m13.579s
sys 0m0.173s
"""