#include <Arduino.h>

const int stepPin = 2;
const int dirPin = 3;

void Driver_Stepper_setup() {
    //sets the two pins as outputs
    pinMode(stepPin,OUTPUT);
    pinMode(dirPin,OUTPUT);
}

void Driver_Stepper_Loop() {
    digitalWrite(dirPin,HIGH);
    //makes 200 pulses for making one full cycle rotation 
    for(int x = 0; x < 200; x++) {
        digitalWrite(stepPin,HIGH);
        delayMicroseconds(500);
        digitalWrite(stepPin,LOW);
        delayMicroseconds(500);
    }
}
