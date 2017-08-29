"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

def is_ascending(num):
	for i in xrange(len(num)-1):
		if num[i] > num[i+1]:
			return False
	return True

def is_descending(num):
	for i in xrange(len(num)-1):
		if num[i] < num[i+1]:
			return False
	return True

percent = 0.99
count = 0
for n in xrange(1, 100000001):
	num = str(n)
	if is_ascending(num):
		continue
	elif is_descending(num):
		continue
	else:
		count += 1
		if float(count)/n == percent:
			print n
			break