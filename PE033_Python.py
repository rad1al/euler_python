"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""


from fractions import Fraction
from math_tools import product

def get_tuples():
    for a in xrange(10,100):
        for b in xrange(10,100):
            if a < b:
                a_str = str(a)
                b_str = str(b)
                a_head = int(a_str[0])
                a_tail = int(a_str[1])
                b_head = int(b_str[0])
                b_tail = int(b_str[1])
                if a_tail == 0 or a_tail != b_head:
                    continue
                x = a * b_tail
                y = b * a_head
                if x == y:
                    yield (a,b)

results = list(get_tuples())
print product([Fraction(t[0], t[1]) for t in results]).denominator

"""
real    0m0.034s
user    0m0.023s
sys 0m0.008s
"""