# What it does: Converts lenna.jpg to grayscale and thresholds it into a binary image
# Wiring:       No wiring needed (image processing only)
# Expected output: Two windows show the grayscale image and the binary image
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/process/binary

import cv2

img = cv2.imread("lenna.jpg",0) # Read the image and convert it to grayscale
cv2.imshow('lenna', img) # Display the image

# Binarize the image
retval, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
