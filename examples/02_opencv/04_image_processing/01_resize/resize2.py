# What it does: Scales lenna.jpg to 0.5x and 2x using the fx and fy arguments
# Wiring:       No wiring needed (image processing only)
# Expected output: Three windows show the original, the 0.5x and the 2x image
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/process/resize

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory
cv2.imshow('lenna', img) # Display the image

img1 = cv2.resize(img, None, fx=1/2 , fy=1/2) # Shrink the image to 1/2 using fx and fy
cv2.imshow('0.5x', img1) # Display the image

img2 = cv2.resize(img, None, fx=2 , fy=2) # Enlarge the image 2x using fx and fy
cv2.imshow('2x', img2) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
