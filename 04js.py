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

# example 2: 
def sum_naturals(n):
	"""sum the first N natural numbers
	>>> sum_naturals(5)
	15
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + k, k+1
	return total 

def sum_cubes(n):
	"""sum the first N cubes of natural numbers. 

	>>> sum_cubes(5)
	225
	"""
	total, k  = 0, 1
	while k <= n:
		total, k = total + pow(k, 3), k+1
	return total 

def sum_pi(n):
	total, k  = 0, 1
	while k<= n:
		total, k = total + 8/ mul(4*k -3, 4*k -1), k+1

### generalize the func sum_naturals, sum_cubes, sum_pi using higher-order func sumation and terms. 
"""pros: express general methods of computation, remove repeatition from program, separate concerns among functions"""

from operator import mul 

def cube(k):	# fcn of a single arg
	return pow(k, 3)  

def pi_term(k):
	return 8/ mul(4*k -3, 4*k -1)

def summation(n, term):  # term is a formal param that will be cound to a function 
	"""sum the first N terms of a sequence

	>>> summation(5, cube)
	225
	"""
	total, k  = 0, 1
	while k <= n:
		total, k = total + term(k), k+1   # term is the fun called here
	return total 


##local defined func: func defined within other function bodies are bound to name in a local frame

def make_adder(n):
	""" return a fcn that takes one  arg K and return k+n 

	>>> add_three = make_adder(3)   ## the name add_three is bound to a function
	>>> add_three(4)
	7

	>>> make_adder(100)(4)
	104
	"""
	def adder(k):
		return k + n
	return adder







