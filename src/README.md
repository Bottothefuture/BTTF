# WRO Future Engineer's Self Driving Vehicle - Open Round Code:
- This folder contains the reference code for the Open Challenge Round using an ESP32
- This code implements logic like steering, motor control and sensor integration to help this vehicle navigate.

---
# FILE OVERVIEW 📂🗂️
```mermaid
flowchart TD;
   A[src]
   B[**Round 1 Code:**
   OpenRoundChallenge]
   C[**Round 2 Code:**
   ObstacleAvoidingChallenge]
   A --> B
   A --> C
   D[**src**]
   E[**RaspberryPi**]
   C --> D
   C --> E
   F[**raspberrypi**]
   G[**src**]
   B --> F
   B --> G
   H[**switch_control.py**]
   F --> H
   I[**main.cpp**]
   G --> I
   J[**ObstacleDetection.py**]
   E --> J
   K[**main.cpp**]
   D-->K
```
### Round 1: OpenRoundChallenge

|FILE|DETAILS|
|----|-------|
|src |The folder containing the code which we upload into the `ESP32`|
|**main.cpp**|The code which is uploaded into the `ESP32` that controls the bot|
|raspberrypi|The folder which is uploaded into the `RaspberryPi`|
|**switch_control.py**|The code which we use for the switch to start the bot|

### Round 2: ObstacleAvoidingChallenge

|FILE|DETAILS|
|----|-------|
|src |The folder containing the code which we upload into the `ESP32`|
|**main.cpp**|The code which is uploaded into the `ESP32` that controls the bot|
|RaspberryPi|The folder which is uploaded into the `RaspberryPi`|
|**ObstacleDetection.py**|The code that `detects obstacles` in the car's path and relays that information to the `ESP32`|

---

# HARDWARE USED ⚙️⚙️
- Microcontroller: [ESP-WROOM-32] **ESP32 Dev Board**
- Steering: **Servo Motor**
- IMU (**BNO055**)
- **Raspberry Pi5**
- **RPi Cam** (For Obstacle Detection In The Second Round)
- Sensors: Ultrasonic Sensors [**One facing front and the other facing to the right**]
- **DC Motor** (Rear Wheel Movement)
- **L298N** Motor Driver
- Battery and Power: (**2x 3.7 Volt Batteries, 1 Li-ion battery**)
---

# HOW TO USE THIS CODE 🧑‍💻🧑‍💻

## Challenge 1: OpenRoundChallenge

### PlatformIO -->
1. Install `PlatformIO` : [**VS Code Extension**]
2. Open the project folder [**OpenRoundChallenge**] in PlatformIO
3. Connect your `ESP32 Board` via USB and in `platformio.ini` confirm your board settings [`board: esp32dev`]
4. **BUILDING & UPLOADING:**
   ```bash
   pio run -- target upload

5. **SETTING UP THE SERIAL MONITOR:**
   ```bash
   pio serial monitor

## Challenge 2: ObstacleAvoidingChallenge

### PlatformIO -->
1. Install `PlatformIO` If You Havent Already : [**VS Code Extension**]
2. Open the project folder [**ObstacleAvoidingChallenge**] in PlatformIO
3. Connect your `ESP32 Board` via USB and in `platformio.ini` confirm your board settings [`board: esp32dev`]
4. **BUILDING & UPLOADING:**
   ```bash
   pio run -- target upload

5. **SETTING UP THE SERIAL MONITOR:**
   ```bash
   pio serial monitor

---

## IMPORTANT INFORMATION 📝📝
--> Tweak angles given in the code to make sure your robot moves straight.
--> You can tweak the values of the if conditions in the turning functions to ensure the vehicles turns accurately
--> Make sure to update the pin numbers in the code to make sure they correspond to the GPIO pins used on the ESP32

---
