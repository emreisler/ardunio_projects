byte recieveData;
int coValue, co2Value;
int digits[10];
char chars[10];

void setup()
{
    Serial.begin(9600);
    
}

void loop()
{   

    coValue = analogRead(A0); // Put ARDUNIO DIY CO2 PPM METER
    co2Value = analogRead(A1); //Put MQ7 sensor

    char cstr1[4];
    char cstr2[4];

    String str1 = String(coValue);
    String str2 = String(co2Value);
    
    str1.toCharArray(cstr1,4);
    str2.toCharArray(cstr2,4);
    
    if(Serial.available() > 0) 
    {
      recieveData = Serial.read();
      if(recieveData == 48){
        for(int i = 0; i < 4; i++){
            
            Serial.print((char)cstr1[i]);
            
            delay(50);
          }
          Serial.print(",");
        for(int i = 0; i < 4; i++){
            
            Serial.print((char)cstr2[i]);
            delay(50);
          }
        }  
    }
}
