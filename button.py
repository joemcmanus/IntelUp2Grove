#!/usr/bin/env python3
# File    : button.py A sample script for the Intel UP^2 board with GrovePi+ shield
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

#This example assumes you have the Grove LED Socket on D8 

import mraa
import time
import argparse 

parser = argparse.ArgumentParser(description='UP^2 GrovePI Button Reader ')
parser.add_argument('--delay', help="Set a delay, defaul 1",  action="store", type=int, default=1)
parser.add_argument('pin', help="The pin the Grove Button is in (D7), i.e. pin 7", type=int)

args=parser.parse_args()

#The UP^2 treats the shield as a sub platform over I2C 
mraa.addSubplatform(mraa.GROVEPI, "0")

#As a sub platform pins start numbering at 512, so D8 is 520
pin=mraa.Gpio(args.pin + 512)

pin.dir(mraa.DIR_IN)

while True:
	print(pin.read())
	time.sleep(args.delay)
