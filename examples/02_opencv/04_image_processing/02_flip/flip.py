# What it does: Flips lenna.jpg along the X axis, the Y axis and both axes at once
# Wiring:       No wiring needed (image processing only)
# Expected output: Four windows show the original, X-flip, Y-flip and XY-flip images
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/process/flip

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory
cv2.imshow('lenna', img) # Display the image

img1 = cv2.flip(img, 0) # Flip along the X axis
cv2.imshow('X', img1) # Display the image

img2 = cv2.flip(img, 1) # Flip along the Y axis
cv2.imshow('Y', img2) # Display the image

img3 = cv2.flip(img, -1) # Flip along both the X and Y axes
cv2.imshow('X & Y', img3) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
