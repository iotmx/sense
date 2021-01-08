#!/usr/bin/env python3
import urllib.request

def is_internet_on():
   try:
      urllib.request.urlopen('http://216.58.200.110', timeout = 2)
      return True
   except:
      pass
   return False

if is_internet_on():
   print ('Internet on')
