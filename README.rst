Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-boardtest/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/boardtest/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_BoardTest/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_BoardTest/actions/
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Board test suite for CircuitPython. Run these tests to ensure that a CircuitPython port was created correctly, individual pin mappings are correct, and buses (e.g. SPI) work.

Tests can be run individually. Copy code found in each *boardtest_<name>.py* module to your CIRCUITPYTHON device drive, and rename the file *code.py*.

Alternatively, tests can be imported as modules. Copy the desired test file to CIRCUITPYTHON device drive and import the test in your own code. Each test can be run with the ``run_test(pins)`` function.

The *boardtest_simpletest.py* (in *examples/*) shows how to call tests from within a script. *boardtest_simpletest.py* runs the following tests:

 * LED Test
 * GPIO Test
 * Voltage Monitor Test
 * UART Test
 * SPI Test
 * I2C Test

Dependencies
=============
This test suite depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `SD Card <https://github.com/adafruit/Adafruit_CircuitPython_SD>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

You will need the following components:

* `Multimeter <https://www.adafruit.com/product/2034>`_
* 1x `LED <https://www.adafruit.com/product/299>`_
* 1x 330 Ohm resistor or `220 Ohm resistor <https://www.adafruit.com/product/2780>`_
* 2x `4.7k Ohm resistor <https://www.adafruit.com/product/2783>`_
* `Microchip 25AA040A SPI EEPROM <https://www.digikey.com/product-detail/en/microchip-technology/25AA040A-I-P/25AA040A-I-P-ND/1212469>`_
* `Microchip AT24HC04B I2C EEPROM <https://www.digikey.com/product-detail/en/microchip-technology/AT24HC04B-PU/AT24HC04B-PU-ND/1886137>`_
* Breadboard
* Wires

Connect the components as shown to your board. Note that you can use a 220 Ohm or 330 Ohm resistor for the LED.

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_BoardTest/blob/main/docs/test_jig.png
    :alt: Test jig Fritzing diagram

To use each test, copy the individual .py or .mpy test(s) into a folder named adafruit_boardtest in the CIRCUITPY drive, import the library, find the pins available on your board, and call ``boardtest_<test name>.run_test(pins)``. To run the GPIO test, for example:

.. code:: python

    import board
    from adafruit_boardtest import boardtest_gpio

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


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/boardtest/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_BoardTest/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
