# What it does: Draws lines, rectangles, a circle and polygons on a 500x500 black canvas
# Wiring:       No wiring needed (image processing only)
# Expected output: A window shows the drawn shapes until a key is pressed
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/draw/shape

import cv2
import numpy as np

# Create a 500x500 RGB888 pure black color image
img = np.zeros((500,500,3),np.uint8)

# Draw a line, from (50,50) to (450,50), red, 5 pixels wide
img = cv2.line(img, (50,50), (450,50), (0,0,255), 5)

# Draw rectangle 1, from (50,80) to (200,200), green, 5 pixels wide
img = cv2.rectangle(img, (50,80), (200,200), (0,255,0), 5)

# Draw rectangle 2, from (250,80) to (450,200), green, filled
img = cv2.rectangle(img, (250,80), (450,200), (0,255,0), -1)

# Draw a circle, center (150,300), radius 50, blue, 3 pixels wide
img = cv2.circle(img, (150, 300), 50, (255,0,0), 5)

# Draw polygon 1, closed
pts = np.array([[50,400],[200,400],[150,480],[50,480]],np.int32)
img = cv2.polylines(img, [pts], True, (255,0,255), 5)

# Draw polygon 2, not closed
pts = np.array([[250,400],[400,400],[350,480],[250,480]],np.int32)
img = cv2.polylines(img, [pts], False, (255,0,255), 5)

cv2.imshow('draw', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the window
