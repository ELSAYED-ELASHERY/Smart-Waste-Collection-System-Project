# Import required libraries
import serial     # Library for serial communication
import time       # Used for delays

# Open the serial port used by the GPS module
# /dev/serial0 is the default UART port on Raspberry Pi
gps = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

print("GPS module started... Waiting for data")

try:

    while True:

        # Read a line of data from the GPS module
        line = gps.readline().decode("utf-8", errors="ignore")

        # GPS sends different NMEA sentences
        # $GPGGA and $GPRMC usually contain position data
        if "$GPGGA" in line or "$GPRMC" in line:

            print("GPS Data:", line.strip())

        # Small delay to avoid CPU overload
        time.sleep(0.1)

except KeyboardInterrupt:

    print("GPS program stopped")

    # Close the serial port
    gps.close()