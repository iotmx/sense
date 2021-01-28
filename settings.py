#Indoor Air Quality Monitor (Wisp)
#by Guillermo Ramirez-Prado
#Settings file

#Environment Box number
currBox                  = 199

#Sample time in seconds
#Temp, Humidity and Atm Pressure Sensor (BME)
st_bme680                = 10
#HPMA
st_hpma                  = 30
#HCHO
st_hcho                  = 10

# Using Bosch BME680 Environmental Sensor  (0 NO, 1 YES)
using_bme680             = 1
# Using Honeywell HPMA115S0 PM Laser Sensor (0 NO, 1 YES)
using_hpma               = 1
# Using DFRobot Gravity HCHO Sensor (0 NO, 1 YES)
using_hcho               = 1

# enable_local enables saving data locally on Wisp uSD card (0 DISABLED, 1 ENABLED)
enable_local             = 1

# Disclaimer:
# when enable_external is enabled Wisp posts data in a database hosted at Unitec.
enable_external          = 1
hosturl                  = "http://dochyper.unitec.ac.nz/Techweek/senddata.php"
headers                  = {'Content-type':'application/x-www-form-urlencoded'}

# Port where HPMA sensor is connected
# (0,1) HPMA jack
mux_s0_hpma              = 1
mux_s1_hpma              = 0
# Port where HCHO sensor is connected
# (0,0) J4, MRX0
# (1,0) HCHO jack
mux_s0_hcho              = 0
mux_s1_hcho              = 0

# Parameters, coefficients and initial conditions

# Coefficients
m25                      = 1
b25                      = 0
m10                      = 1
b10                      = 0

# GPIO BCM ports
tstBtn                   = 4  # GPIO pin 7
mux_s0                   = 27 # GPIO pin 13
mux_s1                   = 22 # GPIO pin 15
conPin                   = 19 # GPIO pin 35
errPin                   = 26 # GPIO pin 37
ackPin                   = 16 # GPIO pin 36
TP2                      = 20 # GPIO pin 38
TP1                      = 21 # GPIO pin 40

# BME680 Adafruit libraries parameters
bme_sea_level_pressure   = 1024
bme_temperature_offset   = -5
