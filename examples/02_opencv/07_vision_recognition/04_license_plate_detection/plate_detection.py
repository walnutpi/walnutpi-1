# What it does: Detects license plates in car.png with a Haar cascade classifier and draws boxes
# Wiring:       No wiring needed (image processing only)
# Expected output: The detected license plates are outlined in red in the result window
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/vision/plate_detection

import cv2

img = cv2.imread('car.png') # Read the image

# Load the license plate detection cascade classifier, the path must not contain Chinese characters
plateFaceCascade = cv2.CascadeClassifier('data/haarcascade_russian_plate_number.xml')

# Detect all the license plates
plates = plateFaceCascade.detectMultiScale(img, 1.15)

# Iterate over every result
for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3) # Draw a box

cv2.imshow('result', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the window
