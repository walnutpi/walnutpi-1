# What it does: Drives an active buzzer on PI15, beeping 5 times
# Wiring:       Connect the active buzzer signal pin to PI15
# Expected output: The buzzer sounds for 0.5s and stays silent for 0.5s, repeated 5 times
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/python/gpio/active_buzzer

import board
import time
from digitalio import DigitalInOut, Direction

# Construct buzzer object and initialize
active_buzzer = DigitalInOut(board.PI15)     # Define pin number
active_buzzer.direction = Direction.OUTPUT   # IO as output

for i in range(5):

    active_buzzer.value = False   # Output low level, turn on the buzzer
    time.sleep(0.5)               # Delay 0.5 second

    active_buzzer.value = True    # Output high level, turn off the buzzer
    time.sleep(0.5)               # Delay 0.5 second
