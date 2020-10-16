usb-thermometer: TEMPer1 and TEMPer1F
===============

### From Pete Chapman:

* Fixed poor precision for TEMPer1F (iProduct string "TEMPer1F_V1.3").

### From Peter Vojtek:

The original version of pcsensor0.0.1 was located on [this page](http://bailey.st/blog/2012/04/12/dirt-cheap-usb-temperature-sensor-with-python-sms-alerting-system/). I took the source code and fixed following bug:

* temperatures below zero overflow: 254.3 C is displayed instead of -1.3 C, . 

### How to run it

1. clone this repository
2. `$ sudo apt-get install libusb-dev`
3. `$ make`
4. connect the thermometer
5. `$ sudo ./pcsensor`

The output looks like:

```
2014/10/30 07:00:36 Temperature 73.96F 23.31C
```


