# What it does: Reads lenna.jpg and saves a copy of it as lenna2.jpg
# Wiring:       No wiring needed (image processing only)
# Expected output: A new file lenna2.jpg is created in the current directory
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/operate

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory
cv2.imwrite('lenna2.jpg', img) # Save the image as lenna2.jpg
