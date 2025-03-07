# wetplant


## BOM
- [raspbeerry pi](https://www.adafruit.com/product/3708)
- [jumper cables](https://www.digikey.com/en/products/filter/jumper-wire/640)
- [SparkFun Soil Moisture Sensor](https://www.sparkfun.com/products/13322)
- [ADS1015](https://www.adafruit.com/product/1083)

## Hardware Setup
- [Connect ADS1015 to Raspberry pi](https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython)
- [Connect Moisture sensor data pin to ADS1015](https://learn.sparkfun.com/tutorials/soil-moisture-sensor-hookup-guide)

## Software Setup
- [configure i2c](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)
- [install Python 3.7 and pip3](https://projects.raspberrypi.org/en/projects/generic-python-install-python3)
- [install ADS1x15](https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15)
- [install CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
- clone this repo

## System Diagram
![image](https://user-images.githubusercontent.com/100881577/164335028-f254804b-b343-4638-8664-fd0adc0ec752.png)

[diagram source](https://lucid.app/lucidchart/2eec7ba2-0517-498e-aeae-fe33b89c26c0/edit?invitationId=inv_d6d0301f-1a2d-41be-aa62-abd66d372e15&page=0_0#)

## Run
```shell
python3 ads_1015.py
```
## Debug
```shell
sudo i2cdetect -y 1
```