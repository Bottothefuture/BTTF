Engineering materials
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2022.

# Content 📁📁

* `t-photos` contains 2 photos of the team (an official one and one funny photo with all team members)
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `video` contains the video.md file with the link to a video where driving demonstration exists
* `schemes` contains one or several schematic diagrams in form of JPEG, PNG or PDF of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `src` contains code of control software for all components which were programmed to participate in the competition
* `models` is for the files for models used by 3D printers, laser cutting machines and CNC machines to produce the vehicle elements. If there is nothing to add to this location, the directory can be removed.
* `other` is for other files which can be used to understand how to prepare the vehicle for the competition. It may include documentation how to connect to a SBC/SBM and upload files there, datasets, hardware specifications, communication protocols descriptions etc. If there is nothing to add to this location, the directory can be removed.
---

# SUMMARY 📝📝
- This project is a **self driving vehicle** which we have designed for the *WRO Future Engineers 2025 Challenge*
- The aim is for the bot to complete the challenges while scoring full points

### KEY FEATURES ‼️:
- We use an IMU (Intertial Measurment Unit) to calculate how many turns the car has taken and to ensure stabilization
- Front wheels are used for steering and the back wheels are using for powering the car.
- The car has two ultrasonic sensors attached to the front of the car. One faces the right and the other faces forward. These ultrasonic sensors dictate how the car moves and detects obstacles in the car's path
- POWER: 2S LiPo for powering the DC Hobby Gear Motor and ESP32, 2x 3.7 Li-Ion Batterys for powering the servo motors.
---

# HARDWARE ⚙️🔩:

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

### Mobility System 🏎️: 
  #### Steering: 
  - **Mechanism**: Front wheels turn to steer.
  - **Actuator**: A precise servo motor.
  - **Implementation**: The servo turns a pivot connected to the wheels, which can still spin freely.
  - **Function**: Lets the wheels roll while accurately controlling the direction of the car.

  #### Motor Drive:
  - **Primary Motor**: A single DC gear motor.
  - **Drive System**: Directly powers the back wheels.
  - **Control Method**: Uses PWM to control speed.
  - **Performance**: Provides steady power for smooth acceleration.

  #### Power: 
  - x2 3.7 Volt Lithium Ion Batteries [These batteries power the servo motor for steering)
  - x1 LiPo Battery [11V] --> Powers the ESP32 and the L298N Motor Driver
  - Powerbank --> Powers the RaspberryPi


  

## TEAM MEMBERS
 * Samesh Deshmukh - samesh.kostub@gmail.com
 * Rohan Mishra  - rohanmishra.email@gmail.com
 * Aadi Khemka - aadikhemka2020@gmail.com


