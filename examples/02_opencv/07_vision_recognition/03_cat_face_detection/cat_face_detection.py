# What it does: Detects cat faces in cat.jpg with a Haar cascade classifier and draws boxes
# Wiring:       No wiring needed (image processing only)
# Expected output: The detected cat faces are outlined in red in the result window
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/vision/cat_face_detection

import cv2

img = cv2.imread('cat.jpg') # Read the image

# Load the cat face detection cascade classifier, the path must not contain Chinese characters
catFaceCascade = cv2.CascadeClassifier('data/haarcascade_frontalcatface.xml')

# Detect all the cat faces
catFaces = catFaceCascade.detectMultiScale(img, 1.15)

# Iterate over every result
for (x, y, w, h) in catFaces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3) # Draw a box

cv2.imshow('result', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the window
