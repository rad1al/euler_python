"""
A bunch of useful mathematical functions.
"""
from math import sqrt
from io_tools import read_data
import operator
from collections import Counter

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

def factorize(x):
    s = set()
    for y in range(1,int(x**0.5)+1):
        if x % y == 0:
            s.update((y,x/y))
    return s

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

def count_factors(n):
    pf = prime_factorize(n)
    count = Counter(pf)
    s = product([v+1 for v in count.values()])
    return s

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

def million_primes():
    return [int(x) for x in read_data("data/primes_up_to_1e6.txt")]

def hundred_million_primes():
    return [int(x) for x in read_data("data/primes_up_to_1e8.txt")]

def get_k_with_largest_v(dct):
    return max(dct.iteritems(), key=operator.itemgetter(1))[0]

def get_k_with_smallest_v(dct):
    return min(dct.iteritems(), key=operator.itemgetter(1))[0]

def triangles(n):
    return [(x*(x+1))/2 for x in xrange(1,n+1)]

def squares(n):
    return [x*x for x in xrange(1,n+1)]

def get_digits(n):
    return [i for i in str(n)]

def int2bin(n):
    return '{0:0b}'.format(n)

def concat(xss):
    return reduce(lambda x,y : x + y, xss)

