# Import required libraries
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C communication with Raspberry Pi
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the ADS1115 ADC module
ads = ADS.ADS1115(i2c)

# Select channel A1 for the ZMPT101B sensor
voltage_channel = AnalogIn(ads, ADS.P1)

print("AC Voltage Sensor Started")

try:
    while True:

        # Read the sensor voltage from ADS1115
        sensor_voltage = voltage_channel.voltage

        # Convert sensor signal to approximate AC voltage
        # This value may require calibration using the potentiometer on the module
        ac_voltage = sensor_voltage * 100

        # Print sensor output
        print(f"Sensor Output Voltage: {sensor_voltage:.3f} V")
        print(f"Estimated AC Voltage: {ac_voltage:.2f} V")
        print("----------------------------")

        # Wait before next reading
        time.sleep(1)

except KeyboardInterrupt:

    print("Program stopped")