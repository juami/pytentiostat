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

class DuplicateDecimals(error)
    """Raised when more than one period is used in an input"""
    pass

class DuplicateNegative(error)
    """Raised when more than one negative sign is used in an input"""
    pass
# This one might be able to be combined with the last one depending on how the code is structured

class ValueOutsidePotentialLimit(error)
    """Raised when input potential is outside the potential bounds of the device"""
    pass

class LowerVoltageEqualsUpperVoltage(error)
    """Raised when inputs in the lower turnover potential and upper turnover potential are equal"""
    pass

class InitialVoltageOutsideUserDefinedPotentialWindow(error)
    """Raised when v_initial is outside the potential window defined by the v_ll and v_ul"""
    pass

class InitialVoltageOutsidePotentialLimit(error)
    """Raised when the v_initial input is outside the potential bounds of the device"""
    pass

class TooManyDecimalPlaces(error)
    """Raised when there are more than two decimal places in the input"""
    pass