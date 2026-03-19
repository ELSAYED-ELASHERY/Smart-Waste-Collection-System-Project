#ifndef DC_MOTER_H
#define DC_MOTER_H

#include <Arduino.h>

// Define DC motor pins (Adjust these according to your electronics wiring)
const int enA = 9;   // PWM pin for speed control
const int in1 = 8;   // Motor direction pin 1
const int in2 = 7;   // Motor direction pin 2

void dc_motor_setup() {
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT); 
  pinMode(in2, OUTPUT);
  
  // Turn off motor - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
}

void dc_motor_forward(int speed) {
  // Set motor speed (0-255)
  analogWrite(enA, speed);
  // Set motor to run forward
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
}

void dc_motor_backward(int speed) {
  // Set motor speed (0-255)
  analogWrite(enA, speed);
  // Set motor to run backward
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
}

void dc_motor_stop() {
  // Stop the motor
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
}

#endif

