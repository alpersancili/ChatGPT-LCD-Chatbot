#include <LiquidCrystal.h>

// Define LCD pins
const int rs = 7, en = 8, d4 = 9, d5 = 10, d6 = 11, d7 = 12;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
    Serial.begin(9600);
    lcd.begin(16, 2);
    lcd.print("Waiting...");
}

void loop() {
    if (Serial.available()) {
        lcd.clear();
        String message = Serial.readStringUntil('\n');
        lcd.setCursor(0, 0);
        
        // Display first 16 characters on first row
        lcd.print(message.substring(0, 16));
        
        // If message is longer, display second part on row 2
        if (message.length() > 16) {
            lcd.setCursor(0, 1);
            lcd.print(message.substring(16, 32));
        }
    }
}








