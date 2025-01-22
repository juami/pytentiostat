.. _instument limitations:

======================
Instrument Limitations
======================

Operational Limitations
========================

Writing Limitations
____________________

#. Voltage from -2.5 V to 2.5 V (Slightly lower from voltage drop in Op-amp)

#. ~20 mV step size (5 V/256 from PWM limitation)

#. PWM Frequency is 31372.55 Hz (Starts new duty cycle every 31.9 microseconds)

Reading Limitations
____________________

#. Voltage ~5 mV step size

#. Resistance resolution dependent on shunt resistor [Will be clarified later]

#. Maximum current dependent on shunt resistor [Will be clarified later]

Read/Write Limitations
_______________________

#. The current standard is 30 ms timestep (6 ms read/write cycle averaged 5 times)

#. Baudrate can transfer data at 115,200 bits/s

Conditional Limitations
========================

Physical Limitations
_____________________

#. Must be connected to laptop for powersource and interfacing.

#. Limited to 2 or 3 electrode setups.

Environmental Limitations
__________________________
#. Temperature range of -40 degC to 85 degC.

:note: Calibrated at room temperature (25 degC) and may need to be recalibrated for different operating
       temperatures.
