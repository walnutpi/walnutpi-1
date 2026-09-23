# What it does: Finds the single best match of the template 2.jpg inside number.jpg
# Wiring:       No wiring needed (image processing only)
# Expected output: A red rectangle marks the matched area in the result window
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/detection/template_match

import cv2
import numpy as np

img = cv2.imread('number.jpg') # Read the source image
temp = cv2.imread('2.jpg') # Read the template image

h, w, c = temp.shape # Get the template image data: height, width and channel count

# Match with the normalized square difference method, the smaller the result the better the match
result = cv2.matchTemplate(img, temp, cv2.TM_SQDIFF_NORMED)

print(result) # Print the result

# Single target matching, minValue is the match result and minLoc is the top-left corner
minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(result)

# Draw a rectangle to show the result
p1 = minLoc # Top-left corner of the rectangle
p2 = (p1[0] + w, p1[1] + h) # Bottom-right corner of the rectangle
cv2.rectangle(img, p1, p2, (0, 0, 255),2)

cv2.imshow('result', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
