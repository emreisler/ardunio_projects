int temperature = 0;
float semi_read = 0;
float final_temp = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  temperature = analogRead(A0);
  semi_read = (temperature/1023.0)*5000;
  final_temp = semi_read/10;
  
  Serial.println(final_temp);
  delay(10);
  Serial.println("15");
  delay(10);
  
}
