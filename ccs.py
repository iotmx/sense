#!/usr/bin/env python
import time

# CCS811 Environmental sensor
from Adafruit_CCS811 import Adafruit_CCS811
ccs =  Adafruit_CCS811()

def ccs811():
   try:
      if ccs.available():
         ccs.readData()
         CO2  = ccs.geteCO2()
         TVOC = ccs.getTVOC()
         print("CO2: {} ppm".format(CO2), "TVOC: {} ppm".format(TVOC))
   except:
      print("Error")

while True:
   ccs811()
   time.sleep(0.1)

