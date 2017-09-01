"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

from math_tools import int2digits

ones = ["one","two","three","four","five","six","seven","eight",
     "nine","ten","eleven","twelve","thirteen","fourteen","fifteen",
     "sixteen","seventeen","eighteen", "nineteen"]
tys = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def first_digit(x):
	return int2digits(x)[0]

def decompose(x):
	if x == 0:
		return ""
	elif x < 20:
		return ones[x - 1]
	elif 20 <= x < 100:
		return tys[first_digit(x) - 2] + decompose(x - first_digit(x) * 10)
	elif x < 1000 and x % 100 == 0:
		return ones[first_digit(x)-1] + "hundred"
	elif 100 < x <= 999:
		return ones[first_digit(x)-1] + "hundredand" + decompose(x-first_digit(x)*100)
	elif x == 1000:
		return "onethousand"

def test_decompose():
	assert decompose(0) == ''
	assert decompose(17) == 'seventeen'
	assert decompose(293) == 'twohundredandninetythree'
	assert decompose(300) == 'threehundred'
	assert decompose(999) == 'ninehundredandninetynine'
	assert decompose(1000) == 'onethousand'
	print "All tests passed."

# test_decompose()

number_names = map(decompose, [x for x in xrange(1,1001)])
ans = sum(map(len, number_names))

print ans

"""
real	0m0.024s
user	0m0.015s
sys	0m0.006s
"""