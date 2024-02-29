void setup(){
  pinMode(11, OUTPUT); 
}
void loop(){
  tone(8, 1000); // Send 1KHz sound signal...
  delay(1000); // ...for 1 sec
  noTone(8); // Stop sound...
  delay(1000); // ...for 1sec
}
