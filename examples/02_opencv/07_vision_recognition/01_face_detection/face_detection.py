# What it does: Detects faces in face1.jpg with a Haar cascade classifier and draws boxes
# Wiring:       No wiring needed (image processing only)
# Expected output: The detected faces are outlined in red in the result window
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/vision/front_face_detection

import cv2

img = cv2.imread('face1.jpg') # Read the image

# Load the face detection cascade classifier, the path must not contain Chinese characters
faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Detect all the faces
faces = faceCascade.detectMultiScale(img, 1.2)

# Iterate over every face result
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3) # Draw a box around the face

cv2.imshow('result', img) # Display the image

cv2.waitKey() # Wait for any key to be pressed
cv2.destroyAllWindows() # Close the window
