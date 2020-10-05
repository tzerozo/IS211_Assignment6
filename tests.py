#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IS211 Week6 (9/28/2020 - 10/5/2020)
#Lang | 10/04/2020 |
#Creating tests is fun but had to reference the reading.

######################################   PartII Tests   ########################

import unittest
import conversions

class KnownValues (unittest.TestCase):
    """ To convert functions inside conversions.py"""
    known_values = (
                        (8.00,46.4,281.15)
                        (16.00,60.8,289.15)
                        (32.00,89.6,305.15),
                        (64.00,147.2,337.15)
                        (128.00,262.4,401.15)
                    )

#####   1.test_c2k  #####
    def test_c2k(self):
        """To test that convertCelsiusToKelvin returns correct converted temperature value. """

        for num in self.known_values:
            Celsius = num[0]
            Kelvin  = num[2]
            result  = conversions.convertCelsiusToKelvin(Celsius)
            self.assertEqual(result, Kelvin,
                            msg=("The result value {} is not the correct & expected value, {}").format(result, Kelvin))

#####   2.test_c2f  #####
    def test_c2f(self):
        """To test that convertCelsiusToFahrenheit returns correct converted temperature value. """

        for num in self.known_values:
            Celsius     = num[0]
            Fahrenheit  = num[1]
            result      = conversions.convertCelsiusToFahrenheit(Fahrenheit)
            self.assertEqual(result, Fahrenheit,
                            msg=("The result value {} is not the correct & expected value,{}").format(result, Fahrenheit))

#####  3.test_f2c  #####
    def test_f2c(self):
        """To test that convertCelsiusToFahrenheit returns correct converted temperature value. """

        for num in self.known_values:
            Fahrenheit  = num[1]
            Celsius     = num[0]
            result      = conversions.convertFahrenheitToCelsius(Celsius)
            self.assertEqual(result, Celsius,
                            msg=("The result value {} is not the correct & expected value,{}").format(result, Celsius))

#####   4.test_f2k  #####
    def test_f2k(self):
        """To test that convertFahrenheitToKelvin returns correct converted temperature value. """

        for num in self.known_values:
            Fahrenheit = num[1]
            Kelvin     = num[2]
            result     = conversions.convertFahrenheitToKelvin(Kelvin)
            self.assertEqual(result, Kelvin,
                            msg=("The result value {} is not the correct & expected value, {}").format(result, Kelvin))

#####  5.test_k2c  #####
    def test_k2c(self):
        """To test that convertKelvinToCelsius returns correct converted temperature value. """

        for num in self.known_values:
            Kelvin  = num[2]
            Celsius = num[0]
            result  = conversions.convertKelvinToCelsius(Celsius)
            self.assertEqual(result, Celsius,
                            msg=("The result value {} is not the correct & expected value,{}").format(result, Celsius))

#####   6.test_k2f  #####
    def test_k2f(self):
        """To test that convertKelvinToFahrenheit returns correct converted temperature value. """

        for num in self.known_values:
            Kelvin      = num[2]
            Fahrenheit  = num[1]
            result      = conversions.convertKelvinToFahrenheit(Fahrenheit)
            self.assertEqual(result, Fahrenheit,
                            msg=("The result value {} is not the correct & expected value,{}").format(result, Fahrenheit))

#####  Main Function #####
if __name__ == "__main__":
    unittest.main()
