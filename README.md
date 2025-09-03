Engineering materials
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2022.

# Table of Contents

1. [Repository Contents](#repository-contents)
2. [Project Summary](#project-summary)
3. [Key Features](#key-features)
4. [Hardware Components](#hardware-components)
5. [Mobility System](#mobility-system)
    1. [Steering](#steering)
    2. [Motor Drive](#motor-drive)
    3. [Power System](#power-system)
6. [Detection System](#detection-system)
    1. [Sensors](#sensors)
    2. [Object Detection Pipeline](#object-detection-pipeline)
7. [Software](#software)
8. [Team Members](#team-members)

---

# Repository Contents

* `t-photos` contains 2 photos of the team (an official one and one funny photo with all team members)
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `video` contains the video.md file with the link to a video where driving demonstration exists
* `schemes` contains one or several schematic diagrams in form of JPEG, PNG or PDF of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `src` contains code of control software for all components which were programmed to participate in the competition
* `models` is for the files for models used by 3D printers, laser cutting machines and CNC machines to produce the vehicle elements. If there is nothing to add to this location, the directory can be removed.
* `other` is for other files which can be used to understand how to prepare the vehicle for the competition. It may include documentation how to connect to a SBC/SBM and upload files there, datasets, hardware specifications, communication protocols descriptions etc. If there is nothing to add to this location, the directory can be removed.

---

# Project Summary

- This project is a **self driving vehicle** which we have designed for the *WRO Future Engineers 2025 Challenge*
- The aim is for the bot to complete the challenges while scoring full points

## Key Features

- We use an IMU (Intertial Measurment Unit) to calculate how many turns the car has taken and to ensure stabilization
- Front wheels are used for steering and the back wheels are using for powering the car.
- The car has two ultrasonic sensors attached to the front of the car. One faces the right and the other faces forward. These ultrasonic sensors dictate how the car moves and detects obstacles in the car's path
- POWER: 2S LiPo for powering the DC Hobby Gear Motor and ESP32, 2x 3.7 Li-Ion Batterys for powering the servo motors.

---

# Hardware Components

### Components:

- **ESP32 Dev Board** --> Microcontroller which controls the motor and makes decisions based on the values given by the ultrasonic sensors.
- **x2 3.7 Volt Lithium Ion Batterys** --> Power the servo motor for steering.
- **x1 LiPo Battery [11V]** --> Powers the ESP32 and the L298N Motor Driver
- **RaspberryPi5** --> Analysis of live video feed.
- **RPi Cam** --> For a live video feed and obstacle detection
- **Powerbank** --> Used for powering the RaspberryPi
- **x2 Ultrasonic Sesnors**: Detect obstacles around the vehicle.
- **DC Hobby Gear Motor** --> Powers the rear-wheels so that the car can move forward and backward.
- **Servo Motor** --> Controls the steering of the car and ensures accurate turning.
- **L298N Motor Driver** --> Controls the DC Hobby Gear Motors and ensures they have the adequate power.
- **IMU [BNO055]** --> Calculates the orientation of the vehicles and feeds that information to the ESP to calculate how many turns have been acheived by the vehicle
- **Step-Down Converter** --> Steps down the voltage to 12V
## Mobility System

### Steering
- **Mechanism**: Front wheels turn to steer.
- **Actuator**: A precise servo motor.
- **Implementation**: The servo turns a pivot connected to the wheels, which can still spin freely.
- **Function**: Lets the wheels roll while accurately controlling the direction of the car.

### Motor Drive
- **Primary Motor**: A single DC gear motor.
- **Drive System**: Directly powers the back wheels.
- **Control Method**: Uses PWM to control speed.
- **Performance**: Provides steady power for smooth acceleration.

### Power System
- x2 3.7 Volt Lithium Ion Batteries (These batteries power the servo motor for steering)
- x1 LiPo Battery [11V] --> Powers the ESP32, L298N Motor Driver and RaspberryPi
- Bug [Step Down] Converter --> Reduces the voltage to 12V to ensure safety of the components

## Detection System

### Sensors
- **x2 UltraSonic Sensors**: Detects obstacles around the vehicle. One is facing right and the other is facing foward
- **IMU (BNO055)**: Checks the orienation of the vehicle and gives feedback to the car. This allows the car to calculate the number of turns it has taken and allows the vehicle to stop accordingly
- **RPi Cam**: Provides a live video feed to the RaspberryPi which is used to detect obstacles.

### Object Detection Pipeline
- **RPi Cam**: Provides us with real-time footage which is then sent to the Raspberry Pi
- **Raspberry Pi**: The Raspberry Pi recieves the footage sent by the `RPi Cam` and analyzes it detecting obstacles using `OpenCV`. The Raspberry Pi then sends this information to the ESP allowing it to adjust the motors suitably
- **UltraSonic Sensors**: Used for `precise wall-detection` to ensure that out car turns and dodges the walls.

# Software

### Video Feed Analysis:
- For processing our video feed we used `Python's OpenCV`
- We used serial communication to establish a data channel between the RaspberryPi and the ESP32. This allowed them to transfer data efficiently and effectively

### Driving Strategies:
- IMU and accurate calculations to ensure that the bot completes the correct amount of turns before stopping
- `Wall Following` and `Corner Detection` to ensure out car is able to steer clear of the walls and stay on the correct path.
     
## Team Members
 * Samesh Deshmukh - samesh.kostub@gmail.com
 * Rohan Mishra  - rohanmishra.email@gmail.com
 * Aadi Khemka - aadikhemka2020@gmail.com


