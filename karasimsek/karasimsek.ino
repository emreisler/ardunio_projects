int leds[] = {2,3,4,5,6};

void setup() {
  // put your setup code here, to run once:

  
  for (int i = 0; i < 5; i ++)
  {
      pinMode(leds[i],OUTPUT);  
  }
  
}

void loop() {
  // put your main code here, to run repeatedly:


  
  for (int i = 0; i < 5; i++)
  {
      digitalWrite(leds[i],HIGH);
      delay(400);
      digitalWrite(leds[i],LOW);
  }

  for (int i = 3; i > 0; i--)
  {
      digitalWrite(leds[i],HIGH);
      delay(400);
      digitalWrite(leds[i],LOW);
  }
  
} 
