# IntelUp2Grove
----
A repo to store example Python scripts for the Intel UP^2 IoT Dev board with the GrovePi+ shield. 

I was not able to find any documentation on using the UP^2 Grove IoT Dev Kit <https://www.seeedstudio.com/UP-Grove-IoT-Development-Kit-p-2994.html> and Python. Currently the wiki is all references for RPi, which this device is not. Hopefully this will help others, I mean it can't hurt, right? 

![alt_tag](https://pbs.twimg.com/media/DrRYbAjU4AAmp2X.jpg)


# Notes
---- 
  - Install python3-mraa 
  - Using the GrovePi+ all the pins start counting from 512, i.e. A0=512 D8=520. 
  - The GrovePi is a subplatform, you will have to initiate it with mraa.addSubplatform(mraa.GROVEPI, "0") 

# Examples
---- 
  - [led.py](led.py) : Blinking an LED with python on D8 and the GrovePi+ wuth UP^2 
  - [temp.py](led.py) : Read the Grove Temp & Humidity Sensor Mini (TH02) with GrovePi+ wuth UP^2

As I get more progress I'll add them here. 

# Useful Links
----
 - https://github.com/intel-iot-devkit/mraa/tree/master/examples/python
 - https://iotdk.intel.com/docs/master/mraa/grovepi.html
 - https://software.intel.com/en-us/iot/hardware/up-squared-grove-dev-kit

# Troubleshooting
----
 If you see the message below, it means you should run the script with sudo. 


    File "./led.py", line 29, in <module>
        pin=mraa.Gpio(520)
      File "/usr/lib/python3.5/dist-packages/mraa.py", line 836, in __init__
        this = _mraa.new_Gpio(pin, owner, raw)

