# What it does: Resizes lenna.jpg to fixed 200x200 and 500x500 using the dsize argument
# Wiring:       No wiring needed (image processing only)
# Expected output: Three windows show the original, the 200x200 and the 500x500 image
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/process/resize

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory
cv2.imshow('lenna', img) # Display the image

img1 = cv2.resize(img, (200,200)) # Resize to 200x200 using the dsize argument
cv2.imshow('200x200', img1) # Display the image

img2 = cv2.resize(img, (500,500)) # Resize to 500x500 using the dsize argument
cv2.imshow('500x500', img2) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
