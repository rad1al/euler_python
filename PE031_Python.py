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

# print cc(200, coins)

"""
real	0m0.909s
user	0m0.898s
sys	0m0.006s
"""

# ---- Dynamic Programming Solution ----

target = 200
coins = [1,2,5,10,20,50,100,200]
# target = 10
# coins = [1,5]
ways = [0]*(target+1)
ways[0] = 1

for i in xrange(len(coins)):
	j = coins[i]
	for j in xrange(coins[i], target+1):
		ways[j] += ways[j - coins[i]]
		j += 1

print ways[-1]
# print ways

"""
real	0m0.016s
user	0m0.009s
sys	0m0.005s
"""