# from smbus2 import SMBus, i2c_msg
# import smbus
# import board
# import busio
# import adafruit_tca9548a

# try:
#     with SMBus(1) as bus:
#         msg = i2c_msg.write(0x70, [0x04, 0x04])
#         bus.i2c_rdwr(msg)
# except Exception as ex:
#     print(ex)
#     print('An error occurred writing to:', hex(0x70))

# initialize i2c bus
# try:
#    bus = smbus.SMBus(1)
# except Exception as ex:
#     print(ex)
#     print("Failed to initialize i2c bus.")

# try:
#     # bus.write_byte(0x70, 0xe1)
#     bus.write_byte(0x70, 0x01)
# except Exception as ex:
#     print(ex)

# class Multiplex:
#     def __init__(self, bus):
#         self.bus = smbus.SMBus(bus)

#     def channel(self, address, channel):
#         if channel == 0: action = 0x01
#         elif channel == 1: action = 0x02
#         elif channel == 2: action = 0x04
#         elif channel == 3: action = 0x08
#         elif channel == 4: action = 0x10
#         elif channel == 5: action = 0x20
#         elif channel == 6: action = 0x40
#         elif channel == 7: action = 0x80
#         else: action = 0x00

#         self.bus.write_byte_data(address, 0x04, action)

# if __name__ == '__main__':
#     bus = 1
#     address = 0x70

#     plexer = Multiplex(bus)
#     plexer.channel(address, 2)

from time import sleep
import board
import busio
import adafruit_tsl2591
import adafruit_tcs34725
import adafruit_tca9548a

# print(board.SCL)
i2c = busio.I2C(board.SCL, board.SDA)
tca = adafruit_tca9548a.TCA9548A(i2c)
# print(tca[0].tca.__dict__.values)

tcs = adafruit_tcs34725.TCS34725(tca[0])
tcs.gain = 60
tcs.integration_time = 100

tsl = adafruit_tsl2591.TSL2591(tca[1])
tsl.gain = adafruit_tsl2591.GAIN_LOW
tsl.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS

while True:
    print('lux:              ', round(tsl.lux, 1))
    print('color_raw:        ', tcs.color_raw)
    print('color_rgb_bytes:  ', tcs.color_rgb_bytes)
    # print('color_temperature:', round(tcs.color_temperature, 1))
    print()
    sleep(2)
