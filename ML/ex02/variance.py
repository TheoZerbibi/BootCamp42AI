import numpy

def mean(x):
	"""Computes the mean of a non-empty numpy.ndarray, using a for-loop.
	Args:
	x: has to be an numpy.ndarray, a vector.
	Returns:
	The mean as a float.
	None if x is an empty numpy.ndarray.
	Raises:
	This function should not raise any Exception.
	"""
	if not type(x) == numpy.ndarray:
		return None;
	sum = 0
	for nb in x:
		sum += nb
	return float(sum/x.size)

def variance(x):
	"""Computes the variance of a non-empty numpy.ndarray, using a for-loop.
	Args:
	x: has to be an numpy.ndarray, a vector.
	Returns:
	The variance as a float.
	None if x is an empty numpy.ndarray.
	Raises:
	This function should not raise any Exception.
	"""
	if not type(x) == numpy.ndarray:
		return None;
	return mean((x - mean(x)) ** 2);

if __name__ == "__main__":
	X = numpy.array([0, 15, -9, 7, 12, 3, -21])
	print(variance(X))
	print(numpy.var(X))
	print(variance(X/2))
	print(numpy.var(X/2))
