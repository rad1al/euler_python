from io_tools import read_data
from math import log

data = read_data("data/PE99_base_exp.txt")
nums = [map(int,row) for row in data]
pairs = [(log(row[0]), row[1]) for row in nums]
prods = {pair[0]*pair[1] : i for i, pair in enumerate(pairs)}
max_prod = max(prods.keys())
index = prods[max_prod]+1
print index