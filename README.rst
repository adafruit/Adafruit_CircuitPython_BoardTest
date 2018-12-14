Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-boardtest/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/boardtest/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_BoardTest.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_BoardTest
    :alt: Build Status

Board test suite for CircuitPython. Run these tests to ensure that a CircuitPython port was created correctly, individual pin mappings are correct, and buses (e.g. SPI) work.

Tests can be run individually. Copy code found in each *boardtest_<name>.py* module to your CIRCUITPYTHON device drive, and rename the file *code.py*.

Alternatively, tests can be imported as modules. Copy the desired test file to CIRCUITPYTHON device drive and import the test in your own code. Each test can be run with the ``run_test(pins)`` function.

The *boardtest_suite.py* (in *examples/*) shows how to call tests from within a script. *boardtest_suite.py* runs the following tests:

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

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_BoardTest/blob/master/docs/test_jig.png
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


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_BoardTest/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-boardtest --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
