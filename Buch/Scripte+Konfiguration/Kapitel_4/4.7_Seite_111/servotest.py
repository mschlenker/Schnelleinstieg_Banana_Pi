#!/usr/bin/python
import RPi.GPIO as GPIO
import time

pin = 16
inc = 0.1
pos = 15.0 # Mitte bei 100Hz

while True:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        Servo = GPIO.PWM(pin, 100)
        Servo.start(pos)
        time.sleep(0.2) # ggf. 0.5
        Servo.stop()
        GPIO.cleanup()
        if (pos > 21.0):
                inc = -0.1
        if (pos < 9.0):
                inc = 0.1
        pos = pos + inc 
        time.sleep(0.1) # ggf. 0.2
