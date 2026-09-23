# What it does: Runs Canny edge detection on lenna.jpg with two different threshold pairs
# Wiring:       No wiring needed (image processing only)
# Expected output: The original image and two edge maps are shown
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/detection/edge_detection

import cv2

img = cv2.imread('lenna.jpg') # Read the image, used to show the original
cv2.imshow('lenna', img) # Display the original image

# Edge detection with the first pair of thresholds
e1 = cv2.Canny(img, 20, 60)
cv2.imshow('e1', e1) # Display the result

# Edge detection with the second pair of thresholds
e2 = cv2.Canny(img, 200, 400)
cv2.imshow('e2', e2) # Display the result

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
