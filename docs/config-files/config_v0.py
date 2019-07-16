# References:
# https://pubs.acs.org/doi/suppl/10.1021/acs.analchem.8b00850/suppl_file/ac8b00850_si_001.pdf
# https://docs.python.org/3/library/configparser.html
# https://pubs.acs.org/doi/pdf/10.1021/acs.jchemed.7b00361
# https://pubs.acs.org/doi/suppl/10.1021/acs.jchemed.7b00361/suppl_file/ed7b00361_si_001.pdf
# https://pdfs.semanticscholar.org/5ac8/4dfb9170928fbf315daf9dab7bf7b07bb95e.pdf
# https://www.researchgate.net/post/What_should_be_the_parameters_for_chronoamperometry_of_FeCl3_solution

# config parameter 1: mode (this will be implemented as a dropdown menu)
# selectable modes: 
    # 1) linear sweep voltammetry - connect the reference and counter electrodes together 
    # 2) chronoamperometry - 
    # 3) cyclic voltammetry -

# mode dependent paramters 
# scan rate [mV/s]
# the potential was varied linearly at the speed of the scan rate. This determines accuracy of cyclic voltammetry measurement


# Example of a config file

import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'mode' : '0',
                     'sampling rate' : '20', # [Hz]
                     'low voltage' : '-0.20', # [V]
                     'high voltage' : '0.80', # [V]
                     'start voltage' : '0.80', # [V]
                     'scan time' : '10'} # [second]

config['linear sweep voltammetry'] = {'mode' : '1',
                           'sampling rate' : '20',
                           'low voltage' : '-0.20',
                           'high voltage' : '0.80',
                           'start voltage' : '0.80',
                           'hold time' : '8',
                           'cycle time' : '30',
                           'step' : '1',
                           'scan rate' : '100'}
                           
config['chronoamperometry'] = {'mode' : '2',
                               'sampling rate' : '20',
                               'scan rate' : '100'}
                               
config['cyclic voltammetry'] = {'mode' : '3',
                                'scan rate': '100'} # [mV/s]


