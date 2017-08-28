# coding: utf8
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from math_tools import uc_numbering
from io_tools import read_data

lst = read_data("data/PE22_names.txt")
lst = reduce(lambda x,y: x+y, lst)

pos = {word : i+1 for i, word in enumerate(sorted(lst))}
assert pos["COLIN"] == 938

print sum([(i+1)*sum(map(lambda x:uc_numbering[x], word)) for i, word in enumerate(sorted(lst))])
