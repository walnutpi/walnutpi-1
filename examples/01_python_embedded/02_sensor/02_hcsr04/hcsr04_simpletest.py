# What it does: Measures distance with an HC-SR04 ultrasonic ranging module
# Wiring:       Connect TRIG to PC9 and ECHO to PC11
# Expected output: The measured distance in cm (2 decimal places) is printed every 0.5 second
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/python/sensor/hcsr04

import time
import board
import adafruit_hcsr04

# Construct the ultrasonic object
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.PC9, echo_pin=board.PC11)

while True:

    try:
        # Print the distance in cm, keep 2 decimal places
        print('%.2f' % sonar.distance + ' cm')

    except RuntimeError:
        print("Retrying!")

    time.sleep(0.5)   # Delay 0.5 second
