#include <Arduino.h>
#include "dc_moter.h"
#include "Driver_Stepper.h"

void setup() {
  // put your setup code here, to run once:
Driver_Stepper_setup();
}

void loop() {
  // put your main code here, to run repeatedly:
  Driver_Stepper_Loop();

  //driver stepper code
  delay(1000); //one second delay
  digitalWrite(dirPin,LOW); //changes the rotation direction 
  //makes 400 pulses for making two full cycle rotation 
  for(int x = 0; x < 200; x++) {
    digitalWrite(stepPin,HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin,LOW);
    delayMicroseconds(500);
  }
}
//------------------------------------------------------------------------