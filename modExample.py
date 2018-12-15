#!/usr/bin/env python3
# File    : example.py - an exmaple of using the groveup moduke
#         : to read the grove button
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  12/11/2018 Joe McManus
# Copyright (C) 2018 Joe McManus

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from groveup import * 
import time
import argparse

parser = argparse.ArgumentParser(description='UP^2 GrovePI Button Reader ')
parser.add_argument('--delay', help="Set a delay, defaul 1",  action="store", type=int, default=1)
parser.add_argument('--pin', help="The pin the sensor is in, i.e. pin 7", type=int)
parser.add_argument('--button', help="Read the Grove Button", action="store_true")
parser.add_argument('--led', help="Toggle the LED", action="store_true")
parser.add_argument('--light', help="Read the Light Sensor", action="store_true")
parser.add_argument('--rotary', help="Read the Rotary Encoder", action="store_true")
parser.add_argument('--temp', help="Read the Temperature Sensor", action="store_true")
parser.add_argument('--lcd', help="Write to the LCD", action="store_true")
parser.add_argument('--lcdOne', help="The message you want to display on line 1 of the LCD", type=str, default="")
parser.add_argument('--lcdTwo', help="The message you want to display on line 2 of the LCD", type=str, default="")
parser.add_argument('--lcdColor', help="Color of the LCD (red|green|blue)", type=str, default="red")

args=parser.parse_args()



#Call initGrove to initialize the GrovePi+ board as abn i2c device. 
initGrove()

if args.rotary or args.light:
	if args.pin == None:
		print("ERROR: Must supply pin number")
		quit()
	print(analogRead(0))

if args.lcd:
	lcdWrite(args.lcdOne, args.lcdTwo, args.lcdColor)	

if args.led:
	pinCheck(args.pin)
	LED(args.pin)

if args.temp:
	temp,hum=temperature()
	print("Temperature: {}°F Humidity: {}%".format(temp,hum))
