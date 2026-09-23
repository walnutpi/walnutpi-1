# What it does: Finds every match of the template 2.jpg inside number.jpg above a threshold
# Wiring:       No wiring needed (image processing only)
# Expected output: Red rectangles mark every matched area and the match count is printed
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/detection/template_match

import cv2
import numpy as np

img = cv2.imread('number.jpg') # Read the source image
temp = cv2.imread('2.jpg') # Read the template image

h, w, c = temp.shape # Get the template image data: height, width and channel count

# Match with the normalized correlation method, the larger the result the better the match
result = cv2.matchTemplate(img, temp, cv2.TM_CCORR_NORMED)

print(result) # Print the result

# Compute the match results and draw the rectangles
num = 0 # Count of match results
for y in range(len(result)): # Iterate over every row
    for x in range(len(result[y])): # Iterate over every column

        if result[y][x] > 0.999: # Adjustable (must be less than 1), the higher the value the better the precision and the fewer the results

            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255),2) # Draw a rectangle

            num = num + 1

print(num)  # Print the match count, try changing the parameter to 0.9 or 0.999 to compare

cv2.imshow('result', img) # Display the result image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
