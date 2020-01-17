from numpy import *

class NumPyCreator:
	def from_list(self, lst, dtype=None):
		"""takes in a list and returns its corresponding NumPy array."""
		return asarray(lst, dtype=dtype, order=None)

	def from_tuple(self, tpl, dtype=None):
		"""takes in a tuple and returns its corresponding NumPy array."""
		return asarray(tpl, dtype=dtype, order=None)

	def from_iterable(self, itr, dtype=None):
		"""takes in an iterable and returns an array which contains all of its elements."""
		return asarray(list(itr), dtype=dtype, order=None)

	def from_shape(self, shape, value=0, dtype=None):
		"""Returns an array filled with the same value.
		First argument is a tuple which specifies the shape of the array,
		and the second argument specifies the value of all elements.
		This value must be 0 by default."""
		return full(shape, value, dtype=dtype)

	def random(self, shape):
		"""Returns an array filled with random values.
		It takes as an argument a tuple which specifies the shape of the array."""
		return random.rand(*shape)

	def identity(self, n, dtype=None):
		"""returns an array representing the identity matrix of size n."""
		return identity(n, dtype=dtype)

if __name__ == '__main__':
	npc = NumPyCreator()
	print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
	print(npc.from_tuple(("a", "b", "c")))
	print(npc.from_iterable(range(5)))
	shape = (3,5)
	print(npc.from_shape(shape))
	print(npc.random(shape))
	print(npc.identity(4))
