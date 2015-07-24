byte zeichen;

void setup() {                
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    zeichen = Serial.read();
    Serial.println(zeichen);
  }
}
