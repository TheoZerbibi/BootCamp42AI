import numpy as np
import sys
import matplotlib.image as mpimg

sys.path.append('/Users/thzeribi/BootCampPython/day03/ex01/')
from ImageProcessor import ImageProcessor

class AdvancedFilter:
	"""
	All methods take in a 3D NumPy array (as in, a tensor of rank 3) and return a modified copy of
	the array.
	The following video should be used as a resource for completing the exercise:
	https://www.youtube.com/watch?v=C_zFhWdM4ic
	BONUS : You can add an optional argument to those methods to choose the kernel size.
	"""

	def mean_blur(self, img, window_size=3):
		"""This method receives an image, performs a mean blur on it and returns a
		blurred copy. In a mean blur, each pixel becomes the average of its neighboring pixels."""
		for x in range (1, img.shape[0]):
			for y in range(1, img.shape[1]):
				pass

if __name__ == '__main__':
	img = mpimg.imread("../ressources/42AI.png")
	af = AdvancedFilter()
	imp = ImageProcessor()
	imp.display(af.mean_blur(img))
