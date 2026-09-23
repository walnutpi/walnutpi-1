# What it does: Detects faces from a USB camera in real time and prints the frame rate
# Wiring:       Connect a USB camera to the board
# Expected output: Faces are boxed in red with the FPS value drawn on the live image, press the space bar to exit
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/vision/front_face_detection

import cv2, time

# Load the face detection cascade classifier, the path must not contain Chinese characters
faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(1) # Open the USB camera

# Lowering the resolution improves the recognition speed, try 480x320 or 320x240
cam.set(3,480) # Set the captured image width to 480
cam.set(4,320) # Set the captured image height to 320


# Calculate FPS (frames per second)
start = 0
end = 0

while True:

    start = time.time() # Record the start time

    retval, img = cam.read() # Read images from the camera in real time

    # Detect all the faces
    faces = faceCascade.detectMultiScale(img, 1.2)
    print(faces)

    # Iterate over every face result
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3) # Draw a box around the face


    end = time.time() # Record the end time

    # Calculate FPS (frames per second), rounded to an integer
    fps = round(1/(end-start))
    print('FPS: ', fps)

    # Write text on the image
    cv2.putText(img, "FPS: "+ str(fps), (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)

    cv2.imshow('result', img) # Display the image

    key = cv2.waitKey(1) # Window refresh interval is 1 millisecond to prevent blocking
    if key == 32: # If the space bar is pressed, break out
        break

cam.release() # Close the camera
cv2.destroyAllWindows() # Destroy the window displaying the camera video
