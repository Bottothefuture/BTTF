import RPi.GPIO as GPIO
import serial
import time


GPIO.setmode(GPIO.BCM)

button_pin = 23
button = False

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.write(b"test\n")
print(ser.readline())

while True:
    button_state = GPIO.input(button_pin)

    if button_state == GPIO.LOW:  # If using PUD_UP, button pressed means LOW
        print("Button Pressed!")
        time.sleep(0.2)  # Debounce delay
        button = True
        ser.write(b"START\n")
        break

    time.sleep(0.1)  # Small delay to prevent busy-waiting
