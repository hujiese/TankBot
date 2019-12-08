int value = 0; 
char flagY = 'S';
char flagY_p = 'S';
char flagX = 'X';
char flagX_p = 'X';
char flagLZ = 'T';
char flagLZ_p = 'T';
char flagRZ = 'T';
char flagRZ_p = 'T';
// Forword: Y--A1 B--D7
// Left: X--A0 B--D8
void setup() 
{ 
  Serial.begin(9600); 
  pinMode(7, INPUT);
  pinMode(8, INPUT);
} 

void loop() 
{ 
  value = analogRead(0); 
  flagX_p = flagX;
  if(value < 200)
  {
    flagX = 'L';//turn left
  }
  else if(value >800)
  {
    flagX = 'R';//turn right  
  }
  else
  {
    flagX = 'X';// stop  
  } 
  if(flagX != flagX_p)
  {
     Serial.print(flagX); 
  }
 
  value = analogRead(1); 
  flagY_p = flagY;
  if(value < 200)
  {
    flagY = 'F';//forward
  }
  else if(value >800)
  {
    flagY = 'B'; //back 
  }
  else
  {
    flagY = 'S'; //stop 
  }
  if(flagY != flagY_p)
  {
     Serial.print(flagY); 
  }

  value = digitalRead(7);
  flagLZ_p = flagLZ;
  if(value == 1)
  {
     flagLZ = 'l'; 
  }
  else
  {
     flagLZ = 'T';
  }
  if(flagLZ_p != flagLZ)
  {
    Serial.print(flagLZ);
  }

  value = digitalRead(8);
  flagRZ_p = flagRZ;
  if(value == 1)
  {
     flagRZ = 'r'; 
  }
  else
  {
     flagRZ = 'T';
  }
  if(flagRZ_p != flagRZ)
  {
    Serial.print(flagRZ);
  }
  delay(100); 
}
