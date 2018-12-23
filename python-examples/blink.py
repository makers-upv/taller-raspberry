#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)

while True:
    GPIO.output(3, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(3, GPIO.LOW)
    time.sleep(0.5)
