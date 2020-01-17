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

	def crop(self, array, dimensions, position=(0,0)):
		"""
		Crop the image as a rectangle with the given dimensions (meaning, the new height and width for the image),
		whose top left corner is given by the position argument.
		The position should be (0,0) by default.
		"""
		#print()
		#print("position[0](y) = " + str(position[0]))
		#print("position[1](x) = " + str(position[1]))
		#print("dimensions[0](y) = " + str(dimensions[0]))
		#print("dimensions[0](x) = " + str(dimensions[1]))
		#print()
		if position[0] > array.shape[0] or dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1] or position[1] > array.shape[1] or dimensions[0] <= 1 or dimensions[1] <= 1 or dimensions[0] <= position[0] or dimensions[0] <= position[1] or dimensions[0] <= position[1] or dimensions[1] <= position[1]:
			raise BaseException(f"The positions {position} + dimensions {dimensions} are greater than the image's dimensions {array.shape[0:2]}")
		return array[position[0]:dimensions[0], position[1]:dimensions[1]]


if __name__ == '__main__':
	imp = ImageProcessor()
	arr = imp.load("../ressources/42AI.png")
	imp.display(arr)
	print(arr)
	sb = ScrapBooker()

	# dimensions.y , dimensions.x - position.y , position.x
	imp.display(sb.crop(arr, (161, 185), position=(145, 15)))
