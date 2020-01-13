import sys

class Params:
	def __init__(self, sum, diff, product, quotient, remaider):
		self.sum = sum
		self.diff = diff
		self.product = product
		self.quotient = quotient
		self.remainder = remainder

def error(nb):
	if nb >= 3 or nb <= 0:
		return "Usage: python operations.py\nExample:\n	python operations.py 10 3"
	error={
			1: 'InputError: too many arguments\n',
			2: 'InputError: only numbers\n'
	}
	return error.get(nb) + "Usage: python operations.py\nExample:\n	python operations.py 10 3"

def print_result(res):
	return ;

def sum(a, b):
	return ;

def diff(a, b):
	return ;

def product(a, b):
	return ;

def quotient(a, b):
	return ;

def remainder(a, b):
	return ;

def operations(a, b):
	return ;

test = int(sys.argv[1])
print(type(test))
print(test)
