# This file is intended to screen all of the user inputs through a series of exceptions defined within a class.

#create a user-defined error called error derived from the Exception class
class error(Exception):
    """Base class for other exceptions"""
    pass

class ValueContainsLetters(error)
    """Raised when the input for numbers includes letters"""
    pass

# this seems to be detected by python already, generating a syntax error

class ValueContainsSpecialChar(error)
    """Raised when the input contains special characters other than "." and "-"."""
    pass

class DuplicateDecimals(error)
    """Raised when more than one period is used in an input"""
    pass

# this seems to already be built into python

class TooManyDecimalPlaces(error)
    """Raised when there are more than two decimal places in the input"""
    pass

# I am thinking if we decide to round to some number of decimal places we can list that the code will automatically round values to that place and then have something that just automatically does this instead of having an error message.

class DuplicateNegative(error)
    """Raised when more than one negative sign is used in an input"""
    pass
# although multiple periods are detected as errors, negatives just combine (for example two negatives = positive) which could be a problem if not detected
# to add to the problem, when this is converted to a string it still does not contain the negative signs


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

