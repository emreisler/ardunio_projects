#define red 6
#define blue 5
#define green 3
int pot_value = 0;
int light_value = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(green,OUTPUT);
  
}

void loop() {
  
  
  pot_value = analogRead(A5);
  Serial.println(pot_value);
  delay(50);
  
  light_value = map(pot_value,0,1023,0,255);
  analogWrite(red,0);
  analogWrite(blue,0);
  analogWrite(green,light_value);
  
  // put your main code here, to run repeatedly:

}
