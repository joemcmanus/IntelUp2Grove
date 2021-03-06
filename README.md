# IntelUp2Grove
----
A repo to store example Python scripts for the Intel UP^2 IoT Dev board with the GrovePi+ shield. 

I was not able to find any documentation on using the UP^2 Grove IoT Dev Kit <https://www.seeedstudio.com/UP-Grove-IoT-Development-Kit-p-2994.html> and Python. Below are sample scripts for (most, soon to be all) sensors in the kit. Thanks for looking and let me know if you need any help 

![alt_tag](https://pbs.twimg.com/media/DrRYbAjU4AAmp2X.jpg)


# Notes
---- 
  - Install python3-mraa 
  - Install python3-upm 
  - Using the GrovePi+ all the pins start counting from 512, i.e. A0=512 D8=520. 
  - The GrovePi is a subplatform, you will have to initiate it with mraa.addSubplatform(mraa.GROVEPI, "0") 

# Examples
---- 
  - [led.py](led.py) : Blinking an LED with python on D8 and the GrovePi+ wuth UP^2 
  - [temp.py](temp.py) : Read the Grove Temp & Humidity Sensor Mini (TH02) with GrovePi+ wuth UP^2
  - [light.py](light.py) : Read the value of the Grove Light Sensor v1.2 with the UP^2 
  - [lcd.py](lcd.py) : Display data and change color on GrovePi+ UP^2 with python 
  - [button.py](button.py) : Read the Grove-Button on GrovePi+ UP^2 with python 

  - [groveup.py](groveup.py) : A python module for the GrovePi+ and Intel UP^2 . 
  - [modExample.py](modExample.py) : Example for using the module


#Module Info
----
First thing import groveup . 

    from groveup import * 


Example script usage: 

    #Print to the LCD 
    joe@squared:~$ sudo ./modExample.py --lcd --lcdOne=Hello --lcdTwo=World --lcdColor=green 
      
    #Read the temperature sensor
    joe@squared:~$ sudo ./modExample.py --temp
    Temperature: 67°F Humidity: 49%


# Useful Links
----
 - https://github.com/intel-iot-devkit/mraa/tree/master/examples/python
 - https://iotdk.intel.com/docs/master/mraa/grovepi.html
 - https://software.intel.com/en-us/iot/hardware/up-squared-grove-dev-kit
 - https://forum.dexterindustries.com/c/grovepi

# Troubleshooting
----
 If you see the message below, it means you should run the script with sudo. 


    File "./led.py", line 29, in <module>
        pin=mraa.Gpio(520)
      File "/usr/lib/python3.5/dist-packages/mraa.py", line 836, in __init__
        this = _mraa.new_Gpio(pin, owner, raw)

