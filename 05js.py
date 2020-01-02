# environments enable higher-order func
def apply_twice(f, x):
	return f(f(x))

def square(x):
	return x*x

result = apply_twice(square, 3)


def repeat(f, x):
	while f(x) != x:
		x = f(x)
	return x

def g(y):
	return (y + 5) // 3

result = repeat(g, 5)  # result = 2

# func composition 

def make_adder(n):
	def adder(k):
		return k+n
	return adder


def triple(x):
	return 3*x

def composel(f, g):
	def h(x):
		return f(g(x))
	return h

squiple = compose1(square, triple)(3) # x = 3 for both square func and triple func
squadder = composel(square, make_adder(2))(3) 

""" squadder = 25 
make_adder(2) return adder func with n = 2, 
composel() return h func with sqaure(x =3), adder(k =3)
"""



