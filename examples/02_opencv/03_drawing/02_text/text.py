# What it does: Draws the text "WalnutPi" on a 500x500 white canvas
# Wiring:       No wiring needed (image processing only)
# Expected output: A window shows the text until a key is pressed
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/draw/string

import cv2
import numpy as np

# Create a 500x500 RGB888 pure white color image
img = np.ones((500,500,3),np.uint8)*255

# Write "WalnutPi" at (20,100), sans-serif font, scale 2, red, thickness 2
cv2.putText(img, 'WalnutPi', (20,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)

cv2.imshow('String', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the window
