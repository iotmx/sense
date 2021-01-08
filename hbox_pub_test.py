#!/usr/bin/env python3
#by Guillermo Ramirez-Prado

import json
import requests
import paho.mqtt.client as mqtt
from hbox_settings import *
from ThingSpeakUpdate import *
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(ackPin, GPIO.OUT)
GPIO.setup(errPin, GPIO.OUT)

GPIO.output(ackPin, GPIO.LOW)
GPIO.output(errPin, GPIO.LOW)

def ack_blink():
    GPIO.output(ackPin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(ackPin, GPIO.LOW)

def err_blink():
    GPIO.output(errPin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(errPin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(errPin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(errPin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(errPin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(errPin, GPIO.LOW)

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_disconnect(mqttc, obj, flags, rc):
    pass

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    try:
        print(enable_post)
        print(localhosturl)
        print(msg.payload)
        print(headers)
        if enable_post and enable_local:
           r = requests.post(localhosturl, data = json.loads(msg.payload), headers = headers )
           print(r.response)
           time.sleep(3)
           if 'error' in r.text:
              err_blink()
           else:
              ack_blink()
           print(r)
        if enable_post and enable_external:
           r = requests.post(hosturl,      data = json.loads(msg.payload), headers = headers )
           if 'error' in r.text:
              err_blink()
           else:
              ack_blink()
    except IOError:
        print("Error")
        err_blink()


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    print("ok")


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("#", 0)

mqttc.loop_forever()
