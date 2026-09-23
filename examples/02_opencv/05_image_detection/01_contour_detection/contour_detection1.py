# What it does: Draws a circle and a rectangle, then finds and outlines their contours
# Wiring:       No wiring needed (image processing only)
# Expected output: Windows show the color, grayscale, binary and contour images in turn
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/detection/contour_detection

import cv2
import numpy as np

# Create a 300x300 RGB888 pure white color image
img = np.ones((300,300,3),np.uint8)*255

# Draw a solid blue circle img0
img0 = cv2.circle(img, (100, 100), 50, (255,0,0), -1)

# Draw a solid red rectangle
img = cv2.rectangle(img0, (150, 150), (250, 250), (0,0,255), -1)

cv2.imshow('color', img) # Display the image

# Convert the color image to a grayscale image (single channel)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img) # Display the image

# Convert the grayscale image to a binary image
t,img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', img) # Display the image

# Detect the contours
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Draw the contours on the original image img0
img = cv2.drawContours(img0, contours, -1, (0,255,0), 5)
cv2.imshow('contours', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
