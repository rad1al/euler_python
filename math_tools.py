"""
A bunch of useful mathematical functions.
"""

def even(n):
    if n % 2 == 0:
        return True
    return False

def odd(n):
    if n % 2 == 1:
        return True
    return False

def prime_factorize(x):
    lst = []
    n = 2
    while True:
        if x == 1:
            return lst
        if x % n == 0:
            lst.append(n)
            x = x/n
            # print(x, n)
        else:
            n += 1