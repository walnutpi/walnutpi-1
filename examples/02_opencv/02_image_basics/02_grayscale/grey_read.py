# What it does: Loads lenna.jpg as a grayscale image, displays it and reads one pixel value
# Wiring:       No wiring needed (image processing only)
# Expected output: A grayscale window is shown and the pixel value is printed
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/image

import cv2

img = cv2.imread("lenna.jpg", 0) # Read lenna.jpg in the current directory and convert it to grayscale
cv2.imshow('grey', img) # Display the image

p = img[315,309] # Read the pixel value at (315,309), 315 is vertical and 309 is horizontal
print(p) # Print the pixel value

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the window
