# What it does: Toggles a relay on PC8 every time the onboard KEY button is pressed
# Wiring:       Connect the relay control pin to PC8
# Expected output: Each KEY press flips the relay state
# Tested on:    WalnutPi 1B
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_1/python/module/relay

import board
import time
from digitalio import DigitalInOut, Direction

# Construct relay object and initialize
relay = DigitalInOut(board.PC8)       # Define pin number
relay.direction = Direction.OUTPUT    # IO as output
relay.value = 1                       # Turn off the relay at startup

# Construct KEY object and initialize
switch = DigitalInOut(board.KEY)      # Define pin number
switch.direction = Direction.INPUT    # IO as input

state = 1   # Relay initial state, high level turns it off

while True:

    if switch.value == 0:             # Key pressed
        time.sleep(0.01)              # Debounce: wait 10ms
        if switch.value == 0:         # Confirm the key is pressed

            state = not state         # Toggle the state
            relay.value = state       # Change the relay state

            # Wait for the key to be released
            while switch.value == 0:
                pass
