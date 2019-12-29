def fib(n):
	"""coumpute the nth Fibonacci number, for N >=1. """
	pred, curr = 1, 0 # 1st, 0th Fibonacci numbers
	k = 0  # curr is the kth Fibonacci number (counter)

	while k < n:
		pred, curr = pred + curr, pred
		k += 1
	return curr 

	# k starts from 0 includes the corner case: K=0 will skip the while loop return curr =0 


"""
function generalization.
"""

from math import pi

def area(r, shape_constant):
	assert r >0 , 'A length must be positive'  # assert evaluate True 
	return r*r*shape_constant

def area_circle(r):
	return area(r, pi)

def area_hexagon(r):
	return area(r, 3*sqrt(3)/2)
