"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

f = open('data/PE13_data.txt', 'r')
data = list(f)
f.close()

nums = [int(x) for x in data]

s = sum(nums)

ans = str(s)[:10]

print ans