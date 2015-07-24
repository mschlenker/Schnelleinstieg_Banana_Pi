#!/bin/bash

echo 23  > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio23/direction
for n in {1..10} ; do
    echo 1 > /sys/class/gpio/gpio23/value
    sleep 0.25
    echo 0 > /sys/class/gpio/gpio23/value
    sleep 0.25
done
echo 23  > /sys/class/gpio/unexport
