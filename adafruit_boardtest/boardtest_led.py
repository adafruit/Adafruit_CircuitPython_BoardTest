# The MIT License (MIT)
#
# Copyright (c) 2018 Shawn Hymel for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_boardtest.boardtest_led`
====================================================
Toggles all available onboard LEDs. You will need to manually verify their
operation by watching them.

Run this script as its own main.py to individually run the test, or compile
with mpy-cross and call from separate test script.

* Author(s): Shawn Hymel for Adafruit Industries

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""
import time

import board
import digitalio
import supervisor

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BoardTest.git"

# Constants
LED_ON_DELAY_TIME = 0.2     # Seconds
LED_OFF_DELAY_TIME = 0.2    # Seconds
LED_PIN_NAMES = ['L', 'LED', 'RED_LED', 'GREEN_LED', 'BLUE_LED']

# Test result strings
PASS = "PASS"
FAIL = "FAIL"
NA = "N/A"

# Release pins
def _deinit_pins(gpios):
    for g in gpios:
        g.deinit()

# Toggle IO pins while waiting for answer
def _toggle_wait(gpios):

    timestamp = time.monotonic()
    led_state = False
    print("Are the pins listed above toggling? [y/n]")
    while True:
        if led_state:
            if time.monotonic() > timestamp + LED_ON_DELAY_TIME:
                led_state = False
                timestamp = time.monotonic()
        else:
            if time.monotonic() > timestamp + LED_OFF_DELAY_TIME:
                led_state = True
                timestamp = time.monotonic()
        for gpio in gpios:
            gpio.value = led_state
        if supervisor.runtime.serial_bytes_available:
            answer = input()
            if answer == 'y':
                return True
            return False

def run_test(pins):

    """
    Toggles the onboard LED(s) on and off.

    :param list[str] pins: list of pins to run the test on
    :return: tuple(str, list[str]): test result followed by list of pins tested
    """

    # Look for pins with LED names
    led_pins = list(set(pins).intersection(set(LED_PIN_NAMES)))

    # Toggle LEDs if we find any
    if led_pins:

        # Print out the LEDs found
        print("LEDs found:", end=' ')
        for pin in led_pins:
            print(pin, end=' ')
        print('\n')

        # Create a list of IO objects for us to toggle
        leds = [digitalio.DigitalInOut(getattr(board, p)) for p in led_pins]

        # Set all LEDs to output
        for led in leds:
            led.direction = digitalio.Direction.OUTPUT

        # Blink LEDs and wait for user to verify test
        result = _toggle_wait(leds)

        # Release pins
        _deinit_pins(leds)

        if result:
            return PASS, led_pins

        return FAIL, led_pins

    # Else (no pins found)
    print("No LED pins found")
    return NA, []

def _main():

    # List out all the pins available to us
    pins = [p for p in dir(board)]
    print()
    print("All pins found:", end=' ')

    # Print pins
    for pin in pins:
        print(pin, end=' ')
    print('\n')

    # Run test
    result = run_test(pins)
    print()
    print(result[0])
    print("Pins tested: " + str(result[1]))

# Execute only if run as main.py or code.py
if __name__ == "__main__":
    _main()
