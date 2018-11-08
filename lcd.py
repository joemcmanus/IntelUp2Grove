#!/usr/bin/env python3
# File    : lcd.py A sample script for the Intel UP^2 board with GrovePi+ shield
#         : using the Grove LCD RGB Backlight . LCD uses an I2C port. 
# Author  : Joe McManus josephmc@alumni.cmu.edu
# Version : 0.1  11/08/2018 Joe McManus
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


from upm import pyupm_jhd1313m1 as lcd
import argparse

parser = argparse.ArgumentParser(description='LCD Example for UP^2 Grove')
parser.add_argument('lineOne', help="The message you want to display on line 1 of the LCD", type=str)
parser.add_argument('lineTwo', help="The message you want to display on line 2 of the LCD", type=str, nargs='?')
parser.add_argument('--color', help="Set the LCD color, i.e. red, green, blue", type=str, default="red")
parser.add_argument('--version', action='version',version='%(prog)s 0.1, (C) Joe McManus josephmc@alumni.cmu.edu')
args=parser.parse_args()


#Initialize the Jhd1313m1 at LCD, LCD is 0x30, RGB 0x62 
lcd = lcd.Jhd1313m1(0, 0x3E, 0x62)


if args.color == "blue":
	lcd.setColor(0,0,255)
if args.color == "red": 
	lcd.setColor(255,0,0)
if args.color == "green":
	lcd.setColor(0,255.0)

#clear screen 
lcd.write("                ");
lcd.write("                ");

#move to first line `
lcd.setCursor(0,0)
lcd.write(args.lineOne)

if args.lineTwo:
	lcd.setCursor(1,0)
	lcd.write(args.lineTwo)

quit()
