import sys

# Define Params List
class Params:
	def __init__(self, sum, diff, product, quotient, remainder):
		self.sum = sum
		self.diff = diff
		self.product = product
		self.quotient = quotient
		self.remainder = remainder

# Check and print error
def print_error(nb):
	if nb >= 3 or nb <= 0:
		print("Usage: python operations.py\nExample:\n	python operations.py 10 3")
		sys.exit()
	error={
			1: 'InputError: too many arguments\n',
			2: 'InputError: only numbers\n'
	}
	print(error.get(nb) + "Usage: python operations.py\nExample:\n	python operations.py 10 3")
	sys.exit()

def get_error():
	if len(sys.argv) <= 1:
		print_error(0)
	elif not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
		print_error(2)
	elif len(sys.argv) >= 4:
		print_error(1)
	else:
		operations(int(sys.argv[1]), int(sys.argv[2]))
	return ;

# Print Result
def print_result(res):
	print("Sum: " + str(res.sum))
	print("Difference: " + str(res.diff))
	print("Product: " + str(res.product))
	print("Quotient: " + str(res.quotient))
	print("Remainder: " + str(res.remainder))
	sys.exit()

# Calculate values
def sum(a, b):
	nbr = a + b
	return nbr;

def diff(a, b):
	nbr = a - b
	return nbr;

def product(a, b):
	nbr = a * b
	return nbr;

def quotient(a, b):
	if b == 0:
		return "ERROR (div by zero)"
	nbr = a / b
	return nbr;

def remainder(a, b):
	if b == 0:
		return "ERROR (modulo by zero)"
	nbr = a % b
	return nbr;

def operations(a, b):
	res = Params(sum(a, b), diff(a,b), product(a, b), quotient(a, b), remainder(a ,b))
	print_result(res)
	return ;

get_error()
