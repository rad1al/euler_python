"""
A bunch of useful mathematical functions.
"""
from math import sqrt

lc_numbering = {item : i+1 for i, item in enumerate("abcdefghijklmnopqrstuvwxyz")}
uc_numbering = {item : i+1 for i, item in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

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

def e_sieve(n):
    multiples = set()
    for k in range(2, n+1):
        if k not in multiples:
            yield k
            multiples.update(range(k*k, n+1, k)) # update set with new elements

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

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def product(lst):
    return reduce(lambda x,y : x*y, lst)

def recursive_powerset(lst):
    if lst == []: # Base case
        return [[]]
    else:
        recursive_result = recursive_powerset(lst[1:]) # apply recursive function to rest of lst
        return recursive_result + [[lst[0]] + item for item in recursive_result] # add the first of lst to every elem in recursive result

def powerset_c(lst):
    """powerset function using comprehensions"""
    output = [[]]
    for item in lst:
        output += [subset+[item] for subset in output]
    return output
