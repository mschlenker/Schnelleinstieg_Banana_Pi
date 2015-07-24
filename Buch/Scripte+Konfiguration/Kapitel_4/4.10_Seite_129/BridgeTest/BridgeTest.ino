#include <Bridge.h>

#define INPUT_PIN A1
#define OUTPUT_PIN 13

int val = 0;

void setup() {
  Bridge.begin(Serial, 19200); 
  pinMode(OUTPUT_PIN, OUTPUT);
}

void loop() {
  val = analogRead(INPUT_PIN);
  Bridge.put("messwert", String(val));
  digitalWrite(OUTPUT_PIN, HIGH); 
  delay(20);  
  digitalWrite(OUTPUT_PIN, LOW); 
  delay(5000);            
}
