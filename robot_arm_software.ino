#include <Servo.h>

Servo servoTaban;
Servo servoOmuz;
Servo servoDirsek;
Servo servoTutamac;
int servoTabanPin = 3;
int servoOmuzPin = 5;
int servoDirsekPin = 6;
int servoTutamacPin = 9;
int joystickSolX = A0;
int joystickSolY = A1;
int joystickSagX = A2;
int joystickSagY = A3;
int joystickSolXValue = 0;
int joystickSolYValue = 0;
int joystickSagXValue = 0;
int joystickSagYValue = 0;
float servoTabanAci = 0;
float servoOmuzAci = 0;
float servoDirsekAci = 0;
float servoTutamacAci = 0;

void setup(){
  //Initilize serial comm ardunio vs computer at 9600 baud rate
  Serial.begin(9600);

  //define servo PWM outputs
  pinMode(servoTabanPin, OUTPUT);
  pinMode(servoOmuzPin, OUTPUT);
  pinMode(servoDirsekPin, OUTPUT);
  pinMode(servoTutamacPin, OUTPUT);

  //Attach pins to servo
  servoTaban.attach(servoTabanPin);
  //servoTaban.write(90);
  servoTutamac.attach(servoTutamacPin);
  //servoTutamac.write(90);
  servoDirsek.attach(servoDirsekPin);
  //servoDirsek.write(90);
  servoOmuz.attach(servoOmuzPin);
  //servoOmuz.write(90);
  
  }

void loop(){
  //read analog inputs 0-1023 from joystick  Dont need to read button switches
  joystickSolXValue = analogRead(joystickSolX);
  joystickSolYValue = analogRead(joystickSolY);
  joystickSagXValue = analogRead(joystickSagX);
  joystickSagYValue = analogRead(joystickSagY);
  
  //map analog inputs 0-1023 to servo angle range 0-180
  servoTabanAci = map(joystickSolXValue,0,1023,0,180); 
  servoOmuzAci = map(joystickSolYValue,0,1023,0,180);
  servoDirsekAci = map(joystickSagXValue,0,1023,0,180);
  servoTutamacAci = map(joystickSagYValue,0,1023,0,180);
  
  // write obtained angles to servo motors
  servoTaban.write(servoTabanAci);
  delay(10);
  servoTutamac.write(servoTutamacAci);
  delay(10);
  servoDirsek.write(servoDirsekAci+30);
  delay(10);
  servoOmuz.write(servoOmuzAci-90);

  //Print to check angles mapped from analog inputs
  //Serial.println(servoTabanAci);
  Serial.println(servoOmuzAci);
  Serial.println(servoDirsekAci);
  //Serial.println(servoTutamacAci);
  //Serial.println(joystickSagYValue);

  
  delay(10);
  }
