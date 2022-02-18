import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import sleep
from dataclasses import dataclass

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)


@dataclass
class Channel:
    voltage: float
    value: int

def get_data():
    return Channel(voltage=chan.voltage, value=chan.value)

def rasp_print(value, voltage):
    print(f"value={value}, voltage={voltage}")

if __name__ == '__main__':
    count = 20
    while count:
        data = get_data()
        rasp_print(data.value, round(data.voltage, 1))
        if data.voltage >= 3.8:
            print("your plant is soaking wet")
        elif data.voltage >= 3.3:
            print("your plant is hydrated")
        elif data.voltage < 3.3:
            print("your plant is dry")
        sleep(2)
        count -= 1
