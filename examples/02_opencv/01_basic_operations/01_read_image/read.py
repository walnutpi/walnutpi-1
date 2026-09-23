# What it does: Reads lenna.jpg from the current directory and prints the image data
# Wiring:       No wiring needed (image processing only)
# Expected output: The image data is printed in the terminal
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/operate

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory
print(img) # Print the image data
