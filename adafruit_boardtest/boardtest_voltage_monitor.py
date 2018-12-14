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
`adafruit_boardtest.boardtest_voltage_monitor`
====================================================
Prints out the measured voltage on any onboard voltage/battery monitor pins.
Note that some boards have an onboard voltage divider to decrease the voltage
to these pins.

Run this script as its own main.py to individually run the test, or compile 
with mpy-cross and call from separate test script.

* Author(s): Shawn Hymel for Adafruit Industries

Implementation Notes
--------------------

**Hardware:**

* `Multimeter <https://www.adafruit.com/product/2034>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import board
import analogio

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BoardTest.git"

# Constants
VOLTAGE_MONITOR_PIN_NAMES = ['VOLTAGE_MONITOR', 'BATTERY']
ANALOG_REF = 3.3            # Reference analog voltage
ANALOGIN_BITS = 16          # ADC resolution (bits) for CircuitPython

# Test result strings
PASS = "PASS"
FAIL = "FAIL"
NA = "N/A"

def run_test(pins):
    
    """
    Prints out voltage on the battery monitor or voltage monitor pin.
    
    :param list[str] pins: list of pins to run the test on
    :return: tuple(str, list[str]): test result followed by list of pins tested
    """
    
    # Look for pins with battery monitoring names
    monitor_pins = list(set(pins).intersection(set(VOLTAGE_MONITOR_PIN_NAMES)))

    # Print out voltage found on these pins
    if monitor_pins:
        
        # Print out the monitor pins found
        print("Voltage monitor pins found:", end=' ')
        for p in monitor_pins:
            print(p, end=' ')
        print('\n')
        
        # Print out the voltage found on each pin
        for p in monitor_pins:
            monitor = analogio.AnalogIn(getattr(board, p))
            voltage = (monitor.value * ANALOG_REF) / (2**ANALOGIN_BITS)
            print(p + ": {:.2f}".format(voltage) + " V")
            monitor.deinit()
        print()
        
        # Ask the user to check these voltages
        print("Use a multimeter to verify these voltages.")
        print("Note that some battery monitor pins might have onboard " +
                "voltage dividers.")
        print("Do the values look reasonable? [y/n]")
        if input() == 'y':
            return PASS, monitor_pins
        else:
            return FAIL, monitor_pins
        
    else:
        print("No battery monitor pins found")
        return NA, []

def _main():
    
    # List out all the pins available to us
    pins = [p for p in dir(board)]
    print()
    print("All pins found:", end=' ')
    
    # Print pins
    for p in pins:
        print(p, end=' ')
    print('\n')

    # Run test
    result = run_test(pins)
    print()
    print(result[0])
    print("Pins tested: " + str(result[1]))

# Execute only if run as main.py or code.py
if __name__ == "__main__":
    _main()
