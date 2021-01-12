#Indoor Air Quality
#by Guillermo Ramirez-Prado
#Settings file

#Environment Box number
currBox        = 200

#Sample time in minutes
#Temp, Humidity and Atm Pressure Sensor (BME)
st_bme680      = 1
#HCHO Sensor
st_hcho        = 1
#HPMA
st_hpma        = 1

# Using the BME  (0 NO, 1 YES)
using_bme680   = 1
# Using the HCHO (0 NO, 1 YES)
using_hcho     = 0
# Using the HPMA (0 NO, 1 YES)
using_hpma     = 1

#{REST}
enable_local    = 0
enable_external = 1
localhosturl    = "http://localhost/senddata.php"
hosturl         = "http://dochyper.unitec.ac.nz/Techweek/senddata.php"
headers         = {'Content-type':'application/x-www-form-urlencoded'}

# GPIO BCM ports
tstBtn = 4  # GPIO pin 7

mux_s0 = 27 # GPIO pin 13
mux_s1 = 22 # GPIO pin 15

conPin = 19 # GPIO pin 35
errPin = 26 # GPIO pin 37
ackPin = 16 # GPIO pin 36

TP2    = 20 # GPIO pin 38
TP1    = 21 # GPIO pin 40


# Coefficients
m25 = 1
b25 = 0

m10 = 1
b10 = 0
