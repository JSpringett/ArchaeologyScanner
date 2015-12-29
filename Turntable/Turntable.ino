/*
  TurnTable

  Controls the turn table for the 3d scanner.
 */

#include <Servo.h> 

Servo servoController; 

// the setup routine runs once when you press reset:
void setup() 
{         
    Serial.begin(19200);
    servoController.attach(9);
    servoController.write(0);
}

// Main loop
void loop() {
    if(Serial.available())
    {       
        int angle = Serial.parseInt();
        Serial.print(angle);
        if(angle >= 0 && angle <= 180)
        {
            servoController.write(angle);
        }   
    } 
}
