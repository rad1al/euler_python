"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n-1)

fac_dict = {'1': 1, '0': 1, '3': 6, '2': 2, '5': 120, '4': 24, '7': 5040, '6': 720, '9': 362880, '8': 40320}

def digit_fac_sum(n):
    return sum([fac_dict[x] for x in str(n)])

def run():
    results = list()
    for i in xrange(3,10000000): # Upper bound is 9,999,999 since 9! * 7 < 9,999,999
        if i == digit_fac_sum(i):
            results.append(i)
    return results

results = run()
print sum(results)

"""
Ran in:

real    0m9.656s
user    0m9.640s
sys     0m0.008s
"""