#!/usr/bin/python
 
import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(16, GPIO.OUT)
for x in range(0, 10):
	GPIO.output(16, GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(16, GPIO.LOW)
	time.sleep(0.25)
GPIO.cleanup()
