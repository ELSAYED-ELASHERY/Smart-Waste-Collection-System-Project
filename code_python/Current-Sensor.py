# Import required libraries
import time                   # Used to create delays
import board                  # Used to access Raspberry Pi pins
import busio                  # Used for I2C communication
import adafruit_ads1x15.ads1115 as ADS    # ADS1115 library
from adafruit_ads1x15.analog_in import AnalogIn  # Used to read analog channels

# Create the I2C interface (SDA and SCL on Raspberry Pi)
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the ADS1115 ADC converter
ads = ADS.ADS1115(i2c)

# Select channel A0 on the ADS1115
channel = AnalogIn(ads, ADS.P0)

# Sensitivity of the ACS712 20A current sensor
sensitivity = 0.100   # 100mV per Ampere

# Idle voltage (2.5V when current = 0)
offset_voltage = 2.5

# Loop to continuously read the current
while True:
    # Read voltage from the sensor
    voltage = channel.voltage

    # Calculate current from the measured voltage
    current = (voltage - offset_voltage) / sensitivity

    # Print the sensor voltage and calculated current
    print(f"Sensor Voltage: {voltage:.3f} V")
    print(f"Measured Current: {current:.3f} A")
    print("----------------------------")

    # Wait 1 second before the next reading
    time.sleep(1)