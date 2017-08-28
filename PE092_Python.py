# coding: utf8
"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

ends_in_mapping = dict()

def number_chain(n):
	return sum(map(lambda x: int(x)**2, list(str(n))))

mappings = dict()

def get_chain(n):
	while True:
		if n == 1 or n == 89:
			return n
		else:
			if n not in mappings:
				mappings[n] = number_chain(n)
				n = number_chain(n)
			else:
				n = mappings[n]


get_chain(145)

def get_ends(n):
	results = list()
	for i in xrange(1,n):
		results.append(get_chain(i))
	return results


lst = get_ends(int(1e7))
print len(filter(lambda x: x != 1, lst))

# Need to optimize later, running time took:
# real	1m36.595s
# user	1m35.741s
# sys	0m0.634s






