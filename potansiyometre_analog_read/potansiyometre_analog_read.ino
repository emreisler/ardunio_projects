#define potpin A5

int deger = 0;

#define led 6

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Pot deger okuma");
  //Direk 5V çıkışada bağlanabilir , deneme amaçlı yapıldı.
  pinMode(led,OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  deger = analogRead(potpin);
  deger = map(deger,0,1023,0,255);
  analogWrite(led, deger);
  Serial.println(deger);
  delay(300);
}
