import sys

class Params:
	def __init__(self, sum, diff, product, quotient, remaider):
		self.sum = sum
		self.diff = diff
		self.product = product
		self.quotient = quotient
		self.remaider = remaider

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

def remaider(a, b):
	return ;

def operations(a, b):

	return ;


if len(sys.argv) <= 1:
	print(error(0))
	exit()
elif len(sys.argv) >= 4:
	print(error(1))
	exit()
if str(sys.argv[1]) or str(sys.argv[2]):
	print(error(2))
	exit()
else:
	operations(sys.argv[1], sys.argv[2])
