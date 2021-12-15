# SPDX-FileCopyrightText: 2018 Shawn Hymel for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_boardtest.boardtest_sd_cd`
====================================================
Reports the output of an SD card's chip detect (CD) pin.

Run this script as its own main.py to individually run the test, or compile
with mpy-cross and call from separate test script.

* Author(s): Shawn Hymel for Adafruit Industries

Implementation Notes
--------------------

**Hardware:**

* `SD Card <https://www.adafruit.com/product/1294>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import board
import digitalio

try:
    from typing import Sequence, Tuple, List
except ImportError:
    pass

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BoardTest.git"

# Constants
SD_CD_PIN_NAME = "SD_CD"

# Test result strings
PASS = "PASS"
FAIL = "FAIL"
NA = "N/A"


def run_test(
    pins: Sequence[str], cd_pin: str = SD_CD_PIN_NAME
) -> Tuple[str, List[str]]:

    """
    Checks status of CD pin as user inserts and removes SD card.

    :param list[str] pins: list of pins to run the test on
    :param str cd_pin: pin name of chip detect (CD) line
    :return: tuple(str, list[str]): test result followed by list of pins tested
    """

    # Ask user to insert and remove SD card
    if list(set(pins).intersection(set([cd_pin]))):

        # Configure CD pin as input with pullup
        cdt = digitalio.DigitalInOut(getattr(board, cd_pin))
        cdt.direction = digitalio.Direction.INPUT
        cdt.pull = digitalio.Pull.UP

        # Tell user to insert SD card
        print("Connect " + cd_pin + " to CD pin on SD card holder.")
        print("Insert SD card into holder.")
        print("Press enter to continue.")
        input()

        # Make sure we see that the pin is low
        if cdt.value:
            print("Error: Card not detected")
            return FAIL, [cd_pin]

        # Tell user to remove SD card
        print("Card detected. Remove card and press enter to continue.")
        input()

        # Make sure we see that the pin is high
        if not cdt.value:
            print("Error: Card detected")
            return FAIL, [cd_pin]

        # Test passed
        print("Card removed")
        return PASS, [cd_pin]

    # Else (no pins found)
    print("No CD pin found")
    return NA, []
