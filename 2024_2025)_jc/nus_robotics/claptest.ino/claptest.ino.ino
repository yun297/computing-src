#include "MeMCore.h"

int clap_count = 0; // Global variable to count claps

void setup() {
  pinMode(A0, INPUT); // Setup A0 under port_4 to detect the mic input
  Serial.begin(9600); // Setup serial monitor for debugging purpose
}

void loop() {
  Detect_Clap(); // Start clap detection immediately
}

void Detect_Clap() {
  int time_now, time_prev1, time_prev2, time_diff1, time_diff2; // Time variables
  int peak = 0, bottom = 1023, current; // Initialize bottom to a value higher than possible initial readings

  // Initialize time_prev2, time_prev1, and time_now
  time_prev2 = time_prev1 = millis(); // Record initial time
  time_now = millis();

  // Initialize time differences
  time_diff1 = time_diff2 = 0;

  // Sample mic and detect claps as long as time_diff2 is within 500ms
  while (time_diff2 >= 0 && time_diff2 < 500) {
    // Update time intervals
    time_now = millis();
    time_diff1 = time_now - time_prev1;
    time_diff2 = time_now - time_prev2;

    // Update time_prev1 and time_prev2
    time_prev1 = time_now;
    time_prev2 = time_prev1;

    // Reset peak and bottom for the current window
    peak = 0;
    bottom = 1023; // Reset bottom to a high value for each iteration

    // Update peak and bottom values within 200ms window
    while (time_diff1 >= 0 && time_diff1 < 200) {
      time_now = millis();
      time_diff1 = time_now - time_prev1;

      // Read mic input
      current = analogRead(A0);

      // Update peak and bottom values
      if (current > peak) {
        peak = current; // Update peak
      }
      if (current < bottom) {
        bottom = current; // Update bottom
      }
    }

    // Check if bottom is still at the initial high value
    if (bottom == 1023) {
      continue; // Skip counting claps until valid readings are obtained
    }

    // Check for clap based on peak-to-bottom amplitude threshold
    if ((peak - bottom) > 700) {
      // Clap detected
      clap_count++; // Increment clap count

      // Print clap count
      Serial.print("Clap detected! Count: ");
      Serial.println(clap_count);

      // Reset bottom to high value after clap detection
      bottom = 1023;
    }
  }
}
