"""
A bunch of useful mathematical functions.
"""
from math import sqrt

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

def check_palindrome(word):
    if len(word) < 2:
        return True
    elif word[0] == word[-1]:
        return True and check_palindrome(word[1:-1])
    else:
        return False

def is_prime(x):
    if x == 0 or x == 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    k = 3
    check_bound = sqrt(x)+1
    while True:
        if k >= check_bound:
            return True
        if x % k == 0:
            return False
        k += 2