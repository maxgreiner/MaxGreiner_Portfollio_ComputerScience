const int buttonPin1 = 13;     // the number of the pushbutton pin
const int buttonPin2 = 12;
const int buttonPin3 = 11;
const int pushbutton = 5;

// variables will change:
int buttonState1 = 0;       
int buttonState2 = 0;       
int buttonState3 = 0;       
int pushbuttonState = 0;       

void setup() {
  // initialize the pushbutton pin as an input:
  Serial.begin(9600);
  pinMode(buttonPin1, INPUT);     
  pinMode(buttonPin2, INPUT);  
  pinMode(buttonPin3, INPUT);  
  pinMode(pushbutton, INPUT);  
}
void loop()
{
  // read the state of the pushbutton value:
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);
  pushbuttonState = digitalRead(pushbutton);
  
  if (pushbuttonState == HIGH)
  {
    Serial.print("Settings");
    for (int x = 0; x<=3; x++)
    {
      Serial.print("Status of Button ");
      Serial.print(x);
      Serial.print(" is ");
      if (x == 0)
      {
        if (buttonState1 == HIGH)
        {
          Serial.print("on ");
        }
      }
      if (x == 0)
      {
        if (buttonState2 == HIGH)
        {
          Serial.print("on ");
        }
      }
      if (x == 0)
      {
        if (buttonState3 == HIGH)
        {
          Serial.print("on ");
        }
      }
     else
     {
       Serial.print("off ");
     }
   
    }
  }

}
