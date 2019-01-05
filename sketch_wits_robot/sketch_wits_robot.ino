#include <Servo.h>

Servo myservo; // create servo object to control a servo
int pos = 0; // variable to store the servo position

const int buzzer = 10; //buzzer to arduino pin 10

const int fsrPin = 0;     // the FSR and 10K pulldown are connected to a0
int fsrReading;     // the analog reading from the FSR resistor divider

void resetHead(void) {
  pos = 80; // default position at 80 degrees
  myservo.write(pos);
}

void shakeHead(void) {
  for (pos = 80; pos <= 125; pos += 1) { // goes from 80 degrees to 125 degrees
    myservo.write(pos); // tell servo to go to position in variable 'pos'
    delay(3); // waits 3ms for the servo to reach the position
  }
  for (pos = 125; pos >= 35; pos -= 1) { // goes from 125 degrees to 35 degrees
    myservo.write(pos); // tell servo to go to position in variable 'pos'
    delay(3); // waits 3ms for the servo to reach the position
  }
  for (pos = 35; pos <= 80; pos += 1) { // goes from 35 degrees to 80 degrees
    myservo.write(pos); // tell servo to go to position in variable 'pos'
    delay(3); // waits 3ms for the servo to reach the position
  }
}

void soundBuzzer(void) {
	tone(buzzer, 8000); // send 8KHz sound signal
	delay(10);
	noTone(buzzer);
}
 
void setup(void) {
  Serial.begin(9600); // send debugging information via the Serial monitor
  myservo.attach(9); // attaches the servo on pin 9 to the servo object
  pinMode(buzzer, OUTPUT); // set buzzer - pin 10 as an output
  resetHead(); // reset head position
}
 
void loop(void) {
  fsrReading = analogRead(fsrPin);  
 
  if (fsrReading > 100) {
    shakeHead();
  }

  if (Serial.available()) {
	int msg = Serial.read();
    if (msg == '1') {
      shakeHead();
    }
	else if (msg == '2') {
		soundBuzzer();
	}
  }
}
