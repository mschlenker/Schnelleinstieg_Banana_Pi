#!/usr/bin/python

import serial
import time

housecode = '\xca\xfe'
unitcode = '\x00'

ser = serial.Serial('/dev/ttyS2', 9600, timeout=1)
for x in range(0, 20):
	ser.write('\x02\x06\xf1')
	ser.write(housecode)
	ser.write(unitcode)
	ser.write('\x12\x00')
	time.sleep(0.10)
	msg = ser.read(4)
	print(msg.encode('hex'))
	time.sleep(3.0)
ser.close()
