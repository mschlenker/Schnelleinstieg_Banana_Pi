#!/usr/bin/python 
from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
 
@app.route("/cam/<pos>")
def cam(pos):
	pin = 16
	n = float(pos)/10
	if (n < 9.0):
		n = 9.0
	if (n > 21.0):
		n = 21.0
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin, GPIO.OUT)
	Servo = GPIO.PWM(pin, 100)
	Servo.start(n)
	time.sleep(0.5)
	Servo.stop()
	GPIO.cleanup()
	return "Servo positioniert!"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
