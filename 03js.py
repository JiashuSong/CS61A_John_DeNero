from operator import floordiv, mod

def divided_exact(n, d=10):
	"""Return the quotient and remainder of dividing N by D.

	>>> q, r = divided_exact(101, 10)
	>>> q
	10
	>>> r
	1

	"""
	return floordiv(n, d), mod(n, d)

# q, r = divided_exact(101, 10)

## add explaination and doctest module. --> python -m doctest -v 03js.py

### satement , boolean context
def abosolute_value(x):
	"""return the abs value of x"""
	if x<0:
		return -x
	elif x == 0:
		return 0
	else:
		return x

###iteration 


