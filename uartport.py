#!/usr/bin/env python3

#Serial port
#by Guillermo Ramirez-Prado

def getrevision():
  # Extract board revision from cpuinfo file
  myrevision = "0000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:8]=='Revision':
        length=len(line)
        myrevision = line[11:length-1]
    f.close()
    print(myrevision)
  except:
    myrevision = "0000"
     
  return myrevision

myrev = getrevision()

ttyserialport   = '/dev/ttyS0'
# Serial port for Raspberry Pi 2
if myrev=="a01041" or myrev=="a21041" or myrev=="a22042":
  ttyserialport   = '/dev/ttyAMA0'
# Serial port for Raspberry Pi 3
if myrev=="a02082" or myrev=="a22082" or myrev=="a32082" or myrev=="a020d3":
  ttyserialport   = '/dev/ttyS0'
print (ttyserialport)
