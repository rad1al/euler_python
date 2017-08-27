"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

from io_tools import read_data
from math import log

data = read_data("data/PE99_base_exp.txt")
nums = [map(int,row) for row in data]
pairs = [(log(row[0]), row[1]) for row in nums]
prods = {pair[0]*pair[1] : i for i, pair in enumerate(pairs)}
max_prod = max(prods.keys())
index = prods[max_prod]+1
print index