#!/usr/bin/python
from flask import Flask, request, send_from_directory
import RPi.GPIO as GPIO
import time
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='/var/cam')

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
        subprocess.call("fswebcam --save /var/cam/cam.jpg -d /dev/video0 -r 1280x960", shell=True)
        html = '<html><body><img src="/static/cam.jpg" width="640" /><br />'
        html = html + '<a href="/cam/90">LL</a> - '
        html = html + '<a href="/cam/125">L</a> - '
        html = html + '<a href="/cam/150">M</a> - '
        html = html + '<a href="/cam/175">R</a> - '
        html = html + '<a href="/cam/210">RR</a>'
        html = html + '</body></html>'
        return html

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
