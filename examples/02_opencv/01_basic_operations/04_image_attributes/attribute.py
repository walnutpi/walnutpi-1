# What it does: Prints the shape, size and dtype of lenna.jpg in color and in grayscale
# Wiring:       No wiring needed (image processing only)
# Expected output: The attributes of the color image and of the grayscale image are printed
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/operate

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory
print('Color image: ')
print('shape: ', img.shape)
print('size: ', img.size)
print('dtype: ', img.dtype)

img = cv2.imread("lenna.jpg", 0) # Read the image and convert it to grayscale
print('Grayscale image: ')
print('shape: ', img.shape)
print('size: ', img.size)
print('dtype: ', img.dtype)
