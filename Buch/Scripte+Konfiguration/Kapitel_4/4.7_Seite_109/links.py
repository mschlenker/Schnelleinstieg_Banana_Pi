#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
Servo = GPIO.PWM(16, 50)
Servo.start(4.0)
print "Links"
time.sleep(0.5) 
Servo.stop()
GPIO.cleanup()
