# What it does: Detects eyes in eye.jpg with a Haar cascade classifier and draws boxes
# Wiring:       No wiring needed (image processing only)
# Expected output: The detected eyes are outlined in red in the result window
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/vision/eye_detection%20copy

import cv2

img = cv2.imread('eye.jpg') # Read the image

# Load the eye detection cascade classifier, the path must not contain Chinese characters
eyeCascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

# Detect all the eyes
eyes = eyeCascade.detectMultiScale(img, 1.2)

# Iterate over every result
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3) # Draw a box

cv2.imshow('result', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the window
