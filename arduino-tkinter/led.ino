char userInput;

#define LED 8
#define LED1 9

void setup(){

  Serial.begin(9600);                        //  setup serial
  pinMode(LED, OUTPUT);
  pinMode(LED1, OUTPUT);

}


void loop(){
  
if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == '0'){                
        digitalWrite(LED, HIGH); 
      }
      if(userInput == '1'){
       digitalWrite(LED, LOW);         
      }
       if(userInput == '2'){                
        digitalWrite(LED1, HIGH); 
      }
      if(userInput == '3'){
       digitalWrite(LED1, LOW);         
      }


  } // Serial.available
} // Void Loop
