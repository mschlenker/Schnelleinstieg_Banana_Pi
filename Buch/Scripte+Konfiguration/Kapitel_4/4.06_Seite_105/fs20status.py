#!/usr/bin/python

import serial
import time

ser = serial.Serial('/dev/ttyS2', 9600, timeout=1)
ser.write('\x02\x01\xf0')
time.sleep(0.20)
msg = ser.read(4)
print(msg.encode('hex'))
ser.close()
