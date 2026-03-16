# Import required libraries
import RPi.GPIO as GPIO     # Library used to control Raspberry Pi GPIO pins
import time                 # Library used to add time delays

# Use BCM pin numbering (GPIO numbers instead of physical pin numbers)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the servo
SERVO_PIN = 18

# Set the pin as an output
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Create a PWM signal on pin 18 with a frequency of 50Hz
# Most servo motors operate at 50Hz
pwm = GPIO.PWM(SERVO_PIN, 50)

# Start PWM with a duty cycle of 0
pwm.start(0)

try:

    while True:

        # For a 360-degree servo:
        # 7.5 ≈ Stop
        # Less than 7.5 = Rotate counterclockwise
        # Greater than 7.5 = Rotate clockwise

        print("Servo rotating right")
        pwm.ChangeDutyCycle(9)   # Rotate right
        time.sleep(3)

        print("Servo stopped")
        pwm.ChangeDutyCycle(7.5) # Stop
        time.sleep(2)

        print("Servo rotating left")
        pwm.ChangeDutyCycle(6)   # Rotate left
        time.sleep(3)

        print("Servo stopped")
        pwm.ChangeDutyCycle(7.5) # Stop
        time.sleep(2)

# If the user presses Ctrl+C
except KeyboardInterrupt:

    # Stop the PWM signal
    pwm.stop()

    # Reset all GPIO pins
    GPIO.cleanup()

    print("Program stopped")