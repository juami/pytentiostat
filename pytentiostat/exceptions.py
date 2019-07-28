# This file is intended to screen all of the user inputs through a series of exceptions defined within a class.

#create a user-defined error called Error derived from the Exception class
class error(Exception):
    """Base class for other exceptions"""
    pass

class ValueContainsLetters(error)
    """Raised when the input for numbers includes letters"""
    pass

class ValueContainsSpecialChar(error)
    """Raised when the input contains special characters other than "." and "-"."""
    pass

class ValueOutsideLimits(error)
    """Raised when input value is outside of the allowable input range"""
    pass


