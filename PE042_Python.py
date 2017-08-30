# coding: utf8
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

from math_tools import triangles, uc_numbering 
from io_tools import read_data

t = set(triangles(100))
data = read_data("data/PE42_words.txt")[0]

def get_sum(w):
	return sum(map(lambda x : uc_numbering[x], w))

total = 0
for word in data:
	if get_sum(word) in t:
		total += 1

print total

"""
real	0m0.024s
user	0m0.013s
sys	0m0.006s
"""