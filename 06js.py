# lambda func

square = lambda x: x*x

def square(x):
	return x*x

def search(f):
	x = 0
	while not f(x):
		x += 1
	return x

def is_three(x):
	return x == 3   # return True or False

def positive(x):
	return max(0, square(x)-100)

def inverse(f):
	"""return g(y) such as g(f(x)) --> x"""

	return lambda y : search(lambda x: f(x) == y)  # only works for perfect squared x. see newton root finding method for details. 


# self reference:

def print_all(x):
	print(x)
	return print_all 


def print_sums(n):
	""" print all sums of args of repeated calls.

	>>> f = print_sums(1)(2)(3)(4)
	1
	3
	6
	10
	"""
	print(n)
	def next_sum(k):
		return print_sums(n+k)
	return next_sum  # return a function next_sum

# control statement: 

if c:
	t
else:
	f

def if_(c, t, f):  # if function.
	if c:
		t
	else: 
		f


from math import sqrt 

def real_sqrt(x):
	"""return real part of the sqaure root of x"""
	if x > 0:
		return sqrt(x)
	else:
		return 0.0

	# return if_(x>0, sqrt(x), 0.0 )  # error because python evaluate each component before call expression. 

#logical Operator , boolean function

def has_big_sqrt(x):
	return x > 0 and sqrt(x) > 10

def reasonable(n):
	return n ==0 or 1/n != 0

# conditional expression: 
""" <consequence> if <predicate> else <alternative> 
	evaluate <predicate> , if true , return <consequence>, otherwise, return <alternative>
"""

abs(1/x if x !=0 else 0)






