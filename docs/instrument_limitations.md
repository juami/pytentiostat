# Instrument Limitations

## Operational Limitations

### Writing Limitations
1. Voltage from -2.5V to 2.5V (Slightly lower from voltage drop off on instrument)
1. ~20mV step size (5V/256 from PWM limitation)
1. PWM Frequency is 31372.55 Hz (Starts new duty cycle every 31.9 microseconds)

### Reading Limitations
1. Voltage ~5mV step size
1. Resistance resolution dependent on shunt resistor [Will be clarified later]
1. Maximum current dependent on shunt resistor [Will be clarified later]

### Read/Write Limitations
1. Current Standard is 30ms timestep (6 ms read/write cycle averaged 5 times)
1. Baudrate can transfer at 115,200 bits/s

## Conditional Limitations

### Physical Limitations
1. Must be connected to laptop for powersource and interfacing
1. Limited to 2 or 3 electrode setups

### Environmental Limitations
1. Temperature range of -40C to 85C
  * Calibrated at room temperature and may need to be recalibrated at different operating temperature
