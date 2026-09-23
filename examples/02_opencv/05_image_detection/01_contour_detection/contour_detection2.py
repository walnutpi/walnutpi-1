# What it does: Finds the contours of lenna.jpg and draws them on the original image
# Wiring:       No wiring needed (image processing only)
# Expected output: Windows show the original, grayscale, binary and contour images in turn
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/detection/contour_detection

import cv2
import numpy as np

img0 = cv2.imread('lenna.jpg') # Read the image, used to show the original
cv2.imshow('lenna', img0) # Display the image

img = cv2.imread('lenna.jpg',0) # Get the grayscale image
cv2.imshow('gray', img) # Display the grayscale image

# Convert the grayscale image to a binary image
t,img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', img) # Display the binary image

# Detect the contours
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Draw the contours on the original image img0
img = cv2.drawContours(img0, contours, -1, (0,255,0), 5)
cv2.imshow('contours', img) # Display the contour image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
