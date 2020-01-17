import numpy as np
import sys

sys.path.append('/Users/thzeribi/BootCampPython/day03/ex01/')
from ImageProcessor import ImageProcessor

class ColorFilter:
	"""
		A tool that can apply a variety of color filters on images.
		For this exercise, the authorized functions and operators are specified for each methods. You
		are not allowed to use anything else.
	"""

	def _dtype_to_int(selfself, array):
		if array.dtype == np.float32:
			array = (array * 255).astype(np.uint8)
		elif array.dtype == np.float64:
			array = (array * 255 * 255).astype(np.uint16)
		return array

	def _blue_mask(self, array):
		array = self._dtype_to_int(array)
		shape_mask = [array.shape[0], array.shape[1], array.shape[2] - 1]
		return np.zeros(shape_mask, dtype=array.dtype)

	def _shading(self, colors, thresholds):
		val_threshold = 256 // thresholds
		for index, val in enumerate(colors):
			for i in range(thresholds):
				if val_threshold * i <= val < val_threshold * (i + 1):
					colors[index] &= val_threshold * i

	def invert(self, array):
		array = self._dtype_to_int(array)
		return -array

	def to_blue(self, array):
		array = self._dtype_to_int(array)
		mask = self._blue_mask(array)
		array[:, :, :2] = mask
		return array

	def to_green(self, array):
		return array[:, :, :] * [0, 1, 0]

	def to_red(self, array):
		return array[:, :, :] * [1, 0, 0]

	def to_celluloid(self, array, n=2):
		array = self._dtype_to_int(array)
		for ext_array in array:
			for colors in ext_array:
				self._shading(colors, n)
		return array

if __name__ == '__main__':
	imp = ImageProcessor()
	arr = imp.load("../ressources/42AI.png")
	cf = ColorFilter()
	invert_arr = cf.invert(arr)
	imp.display(invert_arr)
	imp.display(cf.to_green(arr))
	imp.display(cf.to_red(arr))
	imp.display(cf.to_blue(arr))
	#imp.display(cf.to_celluloid(arr))
	#imp.display(cf.to_celluloid(arr, 8))
	imp.display(cf.to_celluloid(arr, 2))
