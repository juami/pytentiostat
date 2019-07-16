#This file contains all of the user based inputs
import numpy

Circuit_Type = 'RRQRQ' #e.g. 'RC'

Initial_Parameters = [0.4, 0.4, 1*10**-2, 1, 0.4, 1*10**-2, 1] #e. g. [a, b, c, d, e]

Parameter_Lower_Bounds = [0.0, 0.0, 0.0, 0.0, 0.0 , 0.0 , 0.0]

Parameter_Upper_Bounds = [numpy.inf, numpy.inf, numpy.inf, 1.0, numpy.inf, numpy.inf, 1.0]

Filename = 'test.csv' #Should be three columned csv with that contains frequency, real, and imaginary impedance respectively

Frequency_Domain = [0, 1000000] #Lower bound and upper bound of frequency range to consider in Hz
