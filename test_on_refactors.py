#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IS211 Week6 (9/28/2020 - 10/5/2020)  Assignment6
#Lang | 10/04/2020 |
#I will actually start from this file then write conversions_refactored.py

###########################  PartIV Refactor Tests   ####################################
import unittest
import conversions_refactored

class ImpossibleConversion (Exception):
    """ This conversion cannot be done, literally."""
    pass

class ConversionsRefactoredWorking (unittest.TestCase):
    """To convert, using 'convert function' inisde 'conversions_refactored.py' """
    known_values = [
                    ("Celsius"   ,"Fahrenheit",      0,32)
                    ("Celsius"   ,"Kelvin"    ,      0,273.15)
                    ("Fahrenheit","Celsius"   ,     32,0)
                    ("Fahrenheit","Kelvin"    ,      1,255.928)
                    ("Kelvin"    ,"Celsius"   , 273.15,0)
                    ("Kelvin"    ,"Fahrenheit",255.928,1)
                    ("Meters"    ,"Miles"     ,1609.34,1)
                    ("Meters"    ,"Yards"     ,  4.572,5)
                    ("Miles"     ,"Meters"    ,      1,1609.34)
                    ("Miles"     ,"Yards"     ,      1,1760)
                    ("Yards"     ,"Meters"    ,      5,4.572)
                    ("Yards"     ,"Miles"     ,   1760,1)
                    ]
#I mostly struggle with "known_values", to use it as a dict with value-key pairs
#OR use a tuple or list but how to make it work for all the 6 different unit types.

    def test_for_conversion(self):
        """To test that unit conversions are working."""
        for num in self.known_values:
            fromUnit    = val[0]
            toUint      = val[1]
            fromValue   = val[2]
            toValue     = val[3]
            return      = convert(fromUnit, toUnit, fromValue)
            self.assertEqual(return, toValue,
                            msg=("The return value:{} for {} is not the expected value:{}").format(result, toUnit, toValue))

    def test_same(self):
        """To test the same unit type returns same value."""
        for test

    def test_error(self):
        self.assertRaises(ImpossibleConversion,convert,"Celcius", "Miles", 10)

if __name__ == "__main__":
    unittest.main()
