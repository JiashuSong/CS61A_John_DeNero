# test-driven function.

import sys
sys.path.append('./hog')
from ucb import trace


@trace
def gcd(m, n):
	""" Returns the largest k that diveides both m and n, greatest common divider
	k, m, n are all postive integers
	
	>>> gcd(12, 8)
	4
	>>> gcd(16, 12)
	4
	>>> gcd(5, 5)
	5
	>>> gcd(2, 16)
	2
	>>> gcd(16, 8)
	8
	"""

	if m % n == 0:
		return m
	elif m < n:
		return gcd(n, m)
	else:
		return gcd(m-n, n)


# function curring : rediscovered by Haskell Curry, 
# transforming a multi-argument function into a single-argument, higher-order fucntion. 

def make_adder(n):
	return lambda k: n+k

def curry2(f):   # 2 means the function takes 2 arguments
	def g(x):
		def h(y):
			return f(x, y)
		return h
	return g 

curry2 = lambda f: lambda x : lambda y

from operator import add 

"""
>>>m  = curry2(add)
>>>m(2)(3)
5
>>>m(3)(2000)
2003

"""



