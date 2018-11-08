#!/usr/bin/env python3
# File    : temp.py A sample script to read a Grove Temp & Humidity Mini Sensor (TH02) 
#         : on a UP^2 Intel board
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  11/07/2018 Joe McManus
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

#This example assumes you have the Grove Temp Mini sensor Socket on D7

import mraa
import time
from upm import pyupm_th02 as th02

#initialize the Grove Mini Sensor
t=th02.TH02()

while True: 

	temp=round((t.getTemperature() * 9.0 / 5.0) + 32.0)
	hum=round(t.getHumidity())
	print("Temperature: {}°F Humidity: {}%".format(temp,hum))
	time.sleep(5)

