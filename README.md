# IntelUp2Grove
----
A repo to store example Python scripts for the Intel UP^2 IoT Dev board with the GrovePi+ shield. 

I found almost no documentation on using the UP^2 Grove IoT Dev Kit <https://www.seeedstudio.com/UP-Grove-IoT-Development-Kit-p-2994.html> and Python. Currently the wiki all references for RPi, which this device is not, although it uses . 
(https://pbs.twimg.com/media/DrRYbAjU4AAmp2X.jpg)

# Notes
---- 
  - Install python3-mraa 
  - Using the GrovePi+ all the pins start counting from 512, i.e. A0=512 D8=520. 
  - The GrovePi is a subplatform, you will have to initiate it with mraa.addSubplatform(mraa.GROVEPI, "0") 

#Examples
---- 
  - led.py : Blinking an LED with python on D8 and the GrovePi+ wuth UP^2 

As I get more progress I'll add them here. 

