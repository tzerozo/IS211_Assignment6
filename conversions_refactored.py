#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IS211 Week6 (9/28/2020 - 10/5/2020)  Assignment6
#Lang | 10/04/2020 |
#The assignment guide is clear but not that easy to think for answer.

########################   PartIV Refactor Functions  ##########################
#Let's create a new method named 'convert' that takes 3 values.
#fromUnit - the unit we are converting from, as a string
#toUint   - the unit we are converting to, as a string
#value    - the value of fromUnit we are converting fromUnit


def convert (fromUnit, toUnit, value):
    """ Converts from one unit to another.
    Args:
          fromUnit (string) : input unit type, to be converted.
          toUnit   (string) : output unit type, converted.
          value    (float)  : input value, to be converted.
    Returns:
          return    (float) : The converted value.
    Raises:

    Examples:
        >>> convert ("Miles", "Meters", 1)
        1609.34
        >>> convert ("Celsius", "Kelvin", 32)
        305.15

    """
    Unit_Switch = {
        'celsius': {
            'kelvin': lambda x: round((float(x) + 273.15), 2),
            'fahrenheit': lambda x: round(((float(x) * 1.8) + 32), 2)
        },
        'fahrenheit': {
            'kelvin': lambda x: round(((float(x) + 459.67) * 0.5555555556), 2),
            'celsius': lambda x: round(((float(x) - 32.0) * 0.5555555556), 2)
        },
        'kelvin': {
            'fahrenheit': lambda x: round(((float(x) * 1.8) - 459.67), 2),
            'celsius': lambda x: round((float(x) - 273.15), 2)
        },
        'miles': {
            'yards': lambda x: round((float(x) * 1760), 2),
            'meters': lambda x: round((float(x) * 1609.344), 2),
            'feet': lambda x: round((float(x) * 5280), 2)
        },
        'yards': {
            'miles': lambda x: round((float(x) / 1760), 2),
            'meters': lambda x: round((float(x) / 1.094), 2),
            'feet': lambda x: round((float(x) * 3), 2)
        },
        'meters': {
            'miles': lambda x: round((float(x) / 1609.344), 2),
            'yards': lambda x: round((float(x) * 1.094), 2),
            'feet': lambda x: round((float(x) * 3.281), 2)
        },
        'feet': {
            'miles': lambda x: round((float(x) / 5280), 2),
            'yards': lambda x: round((float(x) / 3), 2),
            'meters': lambda x: round((float(x) / 3.281), 2)
        }
    }
#Somehow figuring out for 'Unit_Switch' is not working for me, took forever even with help.
    fromUnit = fromUnit.lower()
    toUnit   = toUnit.lower()
    value    = dec(value)

    if fromUnit == toUnnit:
        return float(value)
    elif toUnit in Unit_Switch[fromUnit]:
        return Unit_Switch[fromUnit] [toUint](value)
    else:
        raise ImpossibleConversion
