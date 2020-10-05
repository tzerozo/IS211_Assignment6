#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IS211 Week6 (9/28/2020 - 10/5/2020)  Assignment6
#Lang | 10/04/2020 |
#The assignment guide is clear (telling there will be 6 functions)
#Had to rethink how I did temps conversion in IS210.

###########################    PartI Functions  ################################
##### 1st Function #####
def convertCelsiusToKelvin(temp):
    """ To converts 'Celcius' to 'Kelvin'.

    Args:
          temp (float) : input value, to be converted.
    Returns:
        return (float) : A value converted to Kelvin.
    Raises:

    Examples:
        >>> convertCelsiusToKelvin(32)
        305.15

    """

    return round((float(temp) + 273.15), 2)


#####  2nd Function #####
def convertCelsiusToFahrenheit(temp):
    """ To converts 'Celcius' to 'Fahrenheit'.

    Args:
              temp (float) : input value, to be converted.
    Returns:
            return (float) : A value converted to Fahrenheit.
    Raises:

    Examples:
            >>> convertCelsiusToFahrenheit(32)
            89.6

    """
    return round (((float(temp) * 1.8) + 32), 2)

#####  3rd Function #####
def convertFahrenheitToCelsius(temp):
    """ To converts 'Fahrenheit' to 'Celcius'.

    Args:
              temp (float) : input value, to be converted.
    Returns:
            return (float) : A value converted to Celsius.
    Raises:

    Examples:
            >>> convertFahrenheitToCelsius(111)
            43.89

    """
    return round (((float(temp) - 32.0) * 0.55555556), 2)
    #instead of using '5/9', I use decimal value of '5/9'.
    #Google put '5/9 as a decimal' equal to '0.55555556'.

#####  4th Function #####
def convertFahrenheitToKelvin(temp):
        """ To converts 'Fahrenheit' to 'Kelvin'.

        Args:
                  temp (float) : input value, to be converted.
        Returns:
                return (float) : A value converted to Kelvin.
        Raises:

        Examples:
                >>> convertFahrenheitToKelvin(111)
                317.03

        """

        return round(((float(temp) + 459.67) * 0.5555555556), 2)

#####  5th Function #####
def convertKelvinToCelsius(temp):
    """ To converts 'Kelvin' to 'Celcius'.

    Args:
              temp (float) : input value, to be converted.
    Returns:
            return (float) : A value converted to Celsius.
    Raises:

    Examples:
            >>> convertKelvinToCelsius(333)
            59.85

    """
    return round((float(temp) - 273.15), 2)

#####  6th Function #####
def convertKelvinToFahrenheit(temp):
    """ To converts 'Kelvin' to 'Fahrenheit'.

    Args:
              temp (float) : input value, to be converted.
    Returns:
            return (float) : A value converted to Fahrenheit.
    Raises:

    Examples:
            >>> convertKelvinToFahrenheit(333)
            139.73

    """
    return round(((float(temp) * 1.8) - 459.67), 2)
