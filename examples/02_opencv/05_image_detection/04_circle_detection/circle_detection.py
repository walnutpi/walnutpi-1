# What it does: Detects circles in circle.jpg with the Hough transform and draws center and ring
# Wiring:       No wiring needed (image processing only)
# Expected output: The circle data is printed and the circles are drawn on the image
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/detection/circle_detection

import cv2
import numpy as np

img0 = cv2.imread('circle.jpg') # Read the image
#cv2.imshow('circle', img0) # Display the original image

# Convert the color image to a grayscale image (single channel)
img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', img1) # Display the image

# Detect the circles
circles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT, 1, 50, 100, 25)

# Round all the coordinates and radii to integers
circles = np.uint(np.around(circles))

print(circles) # Print the circle data

# Draw the circles on the original image
for c in circles[0]:
    x, y, r = c
    cv2.circle(img0, (x, y), 2, (0,255,0), 3) # Draw the center
    cv2.circle(img0, (x, y), r, (0,255,0), 3) # Draw the ring

cv2.imshow('result', img0) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
