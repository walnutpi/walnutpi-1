# What it does: Reads the pixel value at coordinates (315, 309) of lenna.jpg
# Wiring:       No wiring needed (image processing only)
# Expected output: The pixel value is printed in the terminal
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/image

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory

p = img[315,309] # Read the pixel value at (315,309), 315 is vertical and 309 is horizontal

print(p) # Print the pixel value
