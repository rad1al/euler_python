# coding: utf8
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

coins = [1,2,5,10,20,50,100,200]

def cc(amount, coins):
    """Recursive count change function."""
    if amount == 0:
        return 1
    elif amount < 0 or coins == []:
        return 0
    else:
        return cc(amount, coins[:-1]) + cc(amount-coins[-1], coins)

print cc(200, coins)

#> 73682