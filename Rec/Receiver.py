#!/usr/bin/env python

#
# Simplest possible example of using RF24Network,
#
#  RECEIVER NODE
#  Listens for messages from the transmitter and prints them out.
#
from __future__ import print_function
import time
from struct import *
from RF24 import *
from RF24Network import *
import db

# CE Pin, CSN Pin, SPI Speed


radio = RF24(RPI_V2_GPIO_P1_15, RPI_V2_GPIO_P1_24, BCM2835_SPI_SPEED_8MHZ)
network = RF24Network(radio)
db.setupdb()

millis = lambda: int(round(time.time() * 1000))
octlit = lambda n:int(n, 8)

# Address of our node in Octal format (01, 021, etc)
this_node = octlit("00")

# Address of the other node
other_node = octlit("01")

radio.begin()
time.sleep(0.1)
network.begin(90, this_node)    # channel 90
radio.printDetails()
packets_sent = 0
last_sent = 0
while 1:
    network.update()
    while network.available():
        info,message = network.read(32)
        print("Got message: ")
        date,time,flow,volume = message.split(" ")
	print(date,time,flow,volume)
	datetime = date + " " + time + " "
	datetime = str(datetime)
	flow = str(flow)
	volume = str(volume)
    db.insertVariableIntoTable1(datetime, flow, volume)      

