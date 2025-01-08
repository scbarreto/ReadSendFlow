# Read and Send

Python code for communication between Raspberry Pi's using NRF24L01+ using [Newly Optimized RF24Network Layer](http://tmrh20.github.io/RF24Network/classRF24Network.html#ac8e9571bb3d2c20d00955b8f5c15b541). The "Sender" reads the flow from a YS-201F Sensor and sends to "Receiver" using NRF24L01+ transceiver.

## Hardware

* 2x Raspberry Pi 3 Model B (both with 16GB Class 10 microSD card)
* YS-201F Flow Sensor
* Wires
* 10k Resistor
* 2x NRF24L01+ Transceiver (with antenna)
* 2x 10μF electrolytic capacitor

## Installation

* Install [RF24Network](https://github.com/nRF24/RF24Network).
* Compile the C++ code then execute the setup.py scripts to be able to use as a python lib.
* Install sqlite3 (`sudo apt-get install sqlite3`)
* Install screen (`sudo apt-get install screen`)
## Usage
 1. Execute the "Receiver" code (`sudo python Rec/Receiver.py`)
 2. Execute the "Sender" code (`sudo python Send/Sender.py`)


## Pins and Connections

*YS-201F Connections* 
```
Red ------------- 5V

           +----- 3V3
           |
          10K
           |
Yellow ----+----- GPIO23 (BCM Mode) / Pin 16 (BOARD Mode)
Black ----------- Ground
```
*NRF24L01+ Connections* <br/><br/>
Both transceivers have a 10μF electrolytic capacitor between GND and VCC pins (positive lead of the capacitor to GND and the negative lead to VCC).

| NRF24L01+ | Raspberry Pin (BOARD Mode)|
| --- | --- |
| 01 - GND | Pin 25 |
| 02 - VCC | Pin 17 |
| 03 - CE | Pin 15 |
| 04 - CSN | Pin 24 |
| 05 - SCK | Pin 23 |
| 06 - MOSI | Pin 19 |
| 07 - MISO | Pin 21 |
| 08 - IRQ | - |


## Set scripts to start on boot (rc.local) and using screen to see the output

Edit the rc.local file: <br/>
`sudo nano /etc/rc.local`
* Add the following line before line with `exit 0`: <br/>
`screen -dmS receiverscreen sudo python /path/to/Receiver.py $`
* This will open a screen task (screen name: receiverscreen). In order to see the output run:
 `sudo screen -r receiverscreen`
* To minimize the screen without shutting down the script (to detach) press:
`CTRL + a + d`
* To verify if the script is running execute:
`sudo ps -ax | grep python`
* To shut down the script, check the ID with the grep command and execute:
`sudo kill ID`
 
**Repeat all steps for Sender**


