import numpy as np
import sys

sys.path.append('/Users/thzeribi/BootCampPython/day03/ex01/')
from ImageProcessor import ImageProcessor

class ScrapBooker:
	"""
	All methods take in a NumPy array and return a new modified one.
	We are assuming that all inputs are correct, ie,
	you don't have to protect your functions against input errors.
	"""

	def crop(self, array, dimensions, positions=(0,0)):
		"""
		Crop the image as a rectangle with the given dimensions (meaning, the new height and width for the image),
		whose top left corner is given by the position argument.
		The position should be (0,0) by default.
		"""
		dimension = 0
		dimension = np.array(dimensions)
		position = np.array(positions)
		s = np.array(array.shape)[:2]
		if (position > s).any() or (dimension > s).any() or (dimension < position[0]).any() or (dimension < position[1]).any() or (dimension <= 1).any():
			raise BaseException(f"The positions {position} + dimensions {dimensions} are greater than the image's dimensions {array.shape[0:2]}")
		return array[position[0]:dimension[0], position[1]:dimension[1]]

	def thin(self, array, n, axis):
		"""delete ever n-th pixel row along the specified axis(0 vertical, 1 horizontal), example below."""
		if n >= 200 or axis > 1 or n <= 1 or axis < 0:
			raise BaseException("Error, n or axis is invalid")
		return np.delete(array, np.s_[::n], axis)

	def juxtapose(self, array, n, axis=0):
		"""juxtapose n copies of the image along the specified axis (0 vertical, 1 horizontal)."""
		if axis == 1:
			return np.hstack([array for _ in range(n)])
		elif axis == 0:
			return np.vstack([array for _ in range(n)])

	def mosaic(self, array, dimensions):
		"""Make a grid with multiple copies of the array.
		The dimensions argument specifies the dimensions(meaning the height and width) of the grid (e.g. 2x3)."""
		if dimensions[0] <= 0 or dimensions[1] <= 0:
			raise BaseException(f"Invalid dimensions {dimensions[0:2]}")
		result =  self.juxtapose(array, dimensions[0], axis=0)
		return self.juxtapose(result, dimensions[1], axis=1)

if __name__ == '__main__':
	imp = ImageProcessor()
	arr = imp.load("../ressources/42AI.png")
	#imp.display(arr)
	#print(arr)

	sb = ScrapBooker()
	# dimensions.y , dimensions.x - position.y , position.x
	#imp.display(sb.crop(arr, (161, 185), positions=(141, 15)))
	#thinned = sb.thin(arr, n=(199), axis=(1))
	#print(f"Thinned : {thinned.shape}")
	#three_times = sb.juxtapose(arr, 5)
	#print(f"shape of juxtapose: {three_times.shape}")
	#imp.display(three_times)
	#mosaic = sb.mosaic(arr, (10, 5))
	#imp.display(mosaic)
