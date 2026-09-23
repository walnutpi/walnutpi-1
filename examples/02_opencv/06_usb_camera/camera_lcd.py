# What it does: Captures video from a USB camera and shows it full screen on the LCD
# Wiring:       Connect a USB camera and an LCD to the board
# Expected output: Full screen live video is shown on the LCD, press the space bar to exit
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/opencv/lcd

import cv2

# Create a borderless full screen window
cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cam = cv2.VideoCapture(1) # Open the camera

while (cam.isOpened()): # Confirm that it has been opened

    retval, img = cam.read() # Read images from the camera in real time

    cv2.imshow("Video", img) # Display the captured image in a window

    key = cv2.waitKey(1) # Window refresh interval is 1 millisecond to prevent blocking

    if key == 32: # If the space bar is pressed, break out
        break

cam.release() # Close the camera
cv2.destroyAllWindows() # Destroy the window displaying the camera video
