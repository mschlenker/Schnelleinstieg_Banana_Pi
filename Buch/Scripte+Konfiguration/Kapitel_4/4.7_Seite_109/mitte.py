#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
Servo = GPIO.PWM(16, 50)
Servo.start(7.5)
print "Mittelstellung"
time.sleep(0.5) 
Servo.stop()
GPIO.cleanup()
