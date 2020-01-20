import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessor:
	def load(self, path) :
		"""opens the .png file specified by the path argument and returns an array
		with the RGB values of the image pixels. It must display a message specifying
		the dimensions of the image (e.g. 340 x 500)."""
		img = mpimg.imread(path)
		if img.dtype == np.float32:
			img = (img * 255).astype(np.uint8)
		print(f"Loading image of dimensions {img.shape[0:2]}")
		return img

	def display(self, array) :
		"""takes a NumPy array as an argument and displays the corresponding RGB image."""
		plt.imshow(array)
		plt.show()

if __name__ == '__main__':
	imp = ImageProcessor()
	arr = imp.load("../ressources/42AI.png")
	imp.display(arr)
	print(arr.shape)
