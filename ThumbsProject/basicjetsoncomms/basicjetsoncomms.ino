int pin = 8; //change to whatever

void setup() { 
  Serial.begin(9600);
  pinMode(8, INPUT);
}

void loop() {
  if (digitalRead(8)) {
    Serial.println("THUMBS DOWN");
  } else {
    Serial.println("THUMBS UP");
  }
  delay(500);
}
