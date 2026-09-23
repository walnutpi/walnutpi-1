# What it does: Detects straight lines in lines.png with the Hough transform and draws them
# Wiring:       No wiring needed (image processing only)
# Expected output: The line data is printed and the detected lines are drawn on the image
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/detection/line_detection

import cv2
import numpy as np

img0 = cv2.imread('lines.png') # Read the image
cv2.imshow('lines', img0) # Display the original image

# Convert the color image to a grayscale image (single channel)
img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', img1) # Display the image

# Convert the grayscale image to a binary image
t,img2 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('binary', img2) # Display the binary image

# Detect the lines
lines = cv2.HoughLinesP(img2, 1, np.pi/180, 15, 100, 20)

print(lines) # Print the line data

# Draw the lines on the original image
for l in lines:
    x0, y0, x1, y1 = l[0]
    cv2.line(img0, (x0, y0), (x1, y1), (0,255,0), 3)

cv2.imshow('result', img0)

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
