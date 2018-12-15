#!/usr/bin/env python3
# File    : groveup.py - A python module for the GrovePi+ and Intel UP^2
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  12/14/2018 Joe McManus
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

#All of this is built on MRAA
import mraa


#initialize the board
def initGrove():
	#The UP^2 treats the shield as a sub platform over I2C 
	mraa.addSubplatform(mraa.GROVEPI, "0")

#Read an analog sensor like the Light Sensor or trim pot
def analogRead(pin):
	#Add 512 to pin because of sub board
	pin=mraa.Aio(512 + pin)
	return pin.read()

def lcdWrite(lineOne,lineTwo,lcdColor):
	from upm import pyupm_jhd1313m1 as lcd
	#Initialize the Jhd1313m1 as LCD, LCD i2x is  0x30, RGB 0x62 
	lcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
	
	if lcdColor == "blue":
		lcd.setColor(0,0,255)
	if lcdColor == "red": 
		lcd.setColor(255,0,0)
	if lcdColor == "green":
		lcd.setColor(0,255,0)	

	#clear screen 
	lcd.write("                ");
	lcd.write("                ");

	#move to first line 
	lcd.setCursor(0,0)
	lcd.write(lineOne)
	lcd.setCursor(1,0)
	lcd.write(lineTwo)

def LED(pin):
	pin=mraa.Gpio(pin + 512)
	pin.dir(mraa.DIR_IN)
	print(pin.read())
	pin.dir(mraa.DIR_OUT)	
	pin.write(1)
	if pin.read() == 1:
		pin.write(0)
	else: 
		pin.write(1)


def pinCheck(pin): 
	if pin == None:
		print("ERROR: This function requires a pin to be specified.") 
		quit()

def temperature():
	from upm import pyupm_th02 as th02
	t=th02.TH02()
	temp=round((t.getTemperature() * 9.0 / 5.0) + 32.0)
	hum=round(t.getHumidity())
	return(temp,hum)
