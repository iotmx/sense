#!/usr/bin/env python

#by Guillermo Ramirez-Prado

import time
import datetime
import RPi.GPIO as GPIO
from hbox_settings import *

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(conPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(errPin, GPIO.OUT)
GPIO.setup(ackPin, GPIO.OUT)
GPIO.setup(tstBtn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(mux_s0, GPIO.OUT)
GPIO.setup(mux_s1, GPIO.OUT)

GPIO.output(mux_s0,   1)
GPIO.output(mux_s1,   0)

def led_blink():
    GPIO.output(errPin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(errPin, GPIO.LOW)

    GPIO.output(conPin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(conPin, GPIO.LOW)

    GPIO.output(ackPin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ackPin, GPIO.LOW)

def is_internet_on():
   try:
      urllib2.urlopen('http://216.58.200.110', timeout = 2)
      GPIO.output(conPin, GPIO.HIGH)
   except:
      GPIO.output(conPin, GPIO.LOW)

while 1:
   if GPIO.input(tstBtn) == GPIO.HIGH:
      print("Pressed")
   led_blink()
