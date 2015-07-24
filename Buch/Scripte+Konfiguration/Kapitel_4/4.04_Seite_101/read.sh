#!/bin/bash

echo 23 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio23/direction
while true ; do
    val=$( cat /sys/class/gpio/gpio23/value ) 
    if [ $val -gt 0 ] ; then 
        echo 'Schalter gedrückt!'
        sleep 5
    else
        sleep 0.1
    fi
done
