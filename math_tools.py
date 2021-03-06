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

def million_primes(t = int):
    if t == int:
        return [int(x) for x in read_data("data/primes_up_to_1e6.txt")]
    else:
        return read_data("data/primes_up_to_1e6.txt")

def hundred_million_primes(t = int):
    if t == int:
        return [int(x) for x in read_data("data/primes_up_to_1e8.txt")]
    else:
        return read_data("data/primes_up_to_1e8.txt")

def get_k_with_largest_v(dct):
    return max(dct.iteritems(), key=operator.itemgetter(1))[0]

def get_k_with_smallest_v(dct):
    return min(dct.iteritems(), key=operator.itemgetter(1))[0]

def squares(n):
    return [x*x for x in xrange(1,n+1)]

def triangles(n):
    return [(x*(x+1))/2 for x in xrange(1,n+1)]

def pentagons(n):
    return [(x*(3*x-1))/2 for x in xrange(1,n+1)]

def hexagons(n):
    return [(x*(2*x-1)) for x in xrange(1,n+1)]

def get_digits(n):
    return [i for i in str(n)]

def int2bin(n):
    return '{0:0b}'.format(n)

def concat(xss):
    return reduce(lambda x,y : x + y, xss)

def check_perm_s(a,b):
    """Check if 2 strings are permutations of another."""
    if sorted(a) == sorted(b):
        return True
    else:
        return False

def check_perm_n(a,b):
    """Check if 2 integers are permutations of another."""
    tally = [0]*10
    while a > 0:
        n = a % 10
        tally[n] += 1
        a /= 10
    while b > 0:
        n = b % 10
        tally[n] -= 1
        b /= 10
    for i in tally:
        if i != 0:
            return False
    return True


def digits2int(ds):
    """Converts a list or tuple of ints into an integer."""
    n = 0
    k = 1
    i = len(ds) - 1 # Allows it to work for tuples too, whereas 
    while i >= 0:   # original approach with pop() only worked with lists.
        n += k*ds[i]
        k *= 10
        i -= 1
    return n

def int2digits(x):
    """Converts an int to a list of digits."""
    if x == 0:
        return [0]
    digits = list()
    while x > 0:
        digits = [x % 10] + digits
        x /= 10
    return digits

def power(n, x):
    if x > 0 and x % 2 == 0:
        return power(n, x/2) * power(n, x/2)
    elif x % 2 == 1 and x > 2:
        return power(n, x/2) * power(n, x/2) * n
    elif x == 1:
        return n
    elif x == 0:
        return 1





