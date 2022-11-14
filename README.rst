=============
frk_analogout
=============

This is an DAC driver for framework for CircuitPython. It is a light wrapper over the analogio CircuitPython core module.

Usage
-----

In your project conf.py file, include an AnalogOut driver.

.. code-block:: python

    # conf.py
    conf = {
        'DAC':
            {'driver': 'AnalogOut',
             'pin':
                 {'my_dac': 'A0'}
        }
    }