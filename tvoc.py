#!/usr/bin/env python

import time

# CCS811 Environmental sensor
from Adafruit_CCS811 import Adafruit_CCS811
ccs =  Adafruit_CCS811()

def ccs811():
   ccs.readData()
   TVOC = ccs.getTVOC()
   print("TVOC: {} ppm".format(TVOC))

while True:
   ccs811()
   time.sleep(0.1)
