# What it does: Turns the top-left 30x30 pixel block of lenna.jpg green
# Wiring:       No wiring needed (image processing only)
# Expected output: Two windows show the original image and the modified image
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/image

import cv2

img = cv2.imread("lenna.jpg") # Read lenna.jpg in the current directory
cv2.imshow('1', img) # Display the original image

for i in range (30):
    for j in range (30):
        img[i,j] = [0, 255, 0] # Change the pixel to green

cv2.imshow('2', img) # Display the modified image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the windows
