#!/bin/bash

DAEMON="/usr/bin/python2.7"
ARGS="/usr/share/catcam/catcam.py"
PIDFILE="/var/run/catcam.pid"

case "$1" in
  start)
    echo "Starting server"
    /sbin/start-stop-daemon --start --pidfile $PIDFILE \
        --user root --group root \
        -b --make-pidfile \
        --exec $DAEMON $ARGS
    ;;
  stop)
    echo "Stopping server"
    /sbin/start-stop-daemon --stop --pidfile $PIDFILE --verbose
    ;;
  *)
    echo "Usage: /etc/init.d/catcam {start|stop}"
    exit 1
    ;;
esac
exit 0
