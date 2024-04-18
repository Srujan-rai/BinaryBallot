int btnpin1 = 10;
int btnpin2 = 11;
int btnpin3 = 12;
int btnpin4 = 13;

bool canPressButton = false;  

void setup() {
  pinMode(btnpin1, INPUT);
  pinMode(btnpin2, INPUT);
  pinMode(btnpin3, INPUT);
  pinMode(btnpin4, INPUT);

  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    if (input == "yes") {
      canPressButton = true; 
    }
  }

  while (canPressButton) {
    int btn1 = digitalRead(btnpin1);
    int btn2 = digitalRead(btnpin2);
    int btn3 = digitalRead(btnpin3);
    int btn4 = digitalRead(btnpin4);

    if (btn1 == HIGH || btn2 == HIGH || btn3 == HIGH || btn4 == HIGH) {
      if (btn1 == HIGH) {
        Serial.println("1");
        digitalWrite(9, HIGH);
      } else if (btn2 == HIGH) {
        Serial.println("2");
        digitalWrite(8, HIGH);
      } else if (btn3 == HIGH) {
        Serial.println("3");
        digitalWrite(7, HIGH);
      } else if (btn4 == HIGH) {
        Serial.println("4");
        digitalWrite(6, HIGH);
      }

      delay(5000); 
      digitalWrite(9, LOW); 
      digitalWrite(8, LOW);
      digitalWrite(7, LOW);
      digitalWrite(6, LOW);

      canPressButton = false; 
      Serial.println("done");
      delay(1000); 

    }
  }
}
