"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def elim_factors(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] % lst[i] == 0:
                lst[j] = lst[j] / lst[i]
    return lst

def product(lst):
    return reduce(lambda a,b: a*b, lst)

def get_answer(n):
    lst = list(range(1,n+1))
    factors = elim_factors(lst)
    return product(factors)

print int(get_answer(20))