# What it does: Reads lenna.jpg and displays it in a window until a key is pressed
# Wiring:       No wiring needed (image processing only)
# Expected output: A window named "lenna" shows the image and closes on any key press
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/operate

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory
cv2.imshow('lenna', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the window
