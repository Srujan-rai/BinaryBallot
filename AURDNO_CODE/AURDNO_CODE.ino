int btnpin1 = 10;
int btnpin2 = 11;
int btnpin3 = 12;
int btnpin4 = 13;

bool canPressButton = false;  

void setup() {
  pinMode(btnpin1, INPUT_PULLUP);
  pinMode(btnpin2, INPUT_PULLUP);
  pinMode(btnpin3, INPUT_PULLUP);
  pinMode(btnpin4, INPUT_PULLUP);

  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim(); 
    if (input == "yes") {
      canPressButton = true;
      Serial.println("Button press allowed");
    }
  }

  if (canPressButton) {
    int btn1 = digitalRead(btnpin1);
    int btn2 = digitalRead(btnpin2);
    int btn3 = digitalRead(btnpin3);
    int btn4 = digitalRead(btnpin4);

    if (btn1 == LOW) {
      Serial.println("1");
      digitalWrite(9, HIGH);
      delay(3000); 
      digitalWrite(9, LOW);
      canPressButton = false; 
      Serial.println("done");
    } else if (btn2 == LOW) {
      Serial.println("2");
      digitalWrite(8, HIGH);
      delay(3000); 
      digitalWrite(8, LOW);
      canPressButton = false; 
      Serial.println("done");
    } else if (btn3 == LOW) {
      Serial.println("3");
      digitalWrite(7, HIGH);
      delay(3000); 
      digitalWrite(7, LOW);
      canPressButton = false; 
      Serial.println("done");
    } else if (btn4 == LOW) {
      Serial.println("4");
      digitalWrite(6, HIGH);
      delay(3000); 
      digitalWrite(6, LOW);
      canPressButton = false; 
      Serial.println("done");
    }
  }
}
