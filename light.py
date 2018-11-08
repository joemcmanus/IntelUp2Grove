#!/usr/bin/env python3
# File    : light.py A sample script for the Intel UP^2 board with GrovePi+ shield
#         : with the Grove Light Sensor v1.2
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  11/05/2018 Joe McManus
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

parser = argparse.ArgumentParser(description='UP^2 GrovePI Light Sensor Monitor')
parser.add_argument('--delay', help="Set a delay, default 1",  action="store", type=int, default=1)
args=parser.parse_args()

#The UP^2 treats the shield as a sub platform over I2C 
mraa.addSubplatform(mraa.GROVEPI, "0")

#This example assumes it is plugged in to A0 
pin=mraa.Aio(512)

while True:
	print(pin.read())
	time.sleep(args.delay)
