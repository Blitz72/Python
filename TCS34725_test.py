# import smbus
# from time import sleep
# 
# channel = 1
# address1 = 0x29
# TCS34725_ENABLE = 0x00
# TCS34725_ENABLE_AIEN = 0x10
# 
# 
# try:
#    bus = smbus.SMBus(channel)
# except Exception as ex:
#     print(ex)
#     print("Tried to initialize i2c bus.")
# 
# 
# try:
#     reg_value = bus.read_byte_data(address1, TCS34725_ENABLE)
#     reg_value &= ~TCS34725_ENABLE_AIEN
#     reg_value |= 0x66
# #    reg_value = TCS34725_ENABLE & ~TCS34725_ENABLE_AIEN
#     print('reg_value to write: ', reg_value)
#     bus.write_byte_data(address1, TCS34725_ENABLE, reg_value)
# except Exception as ex:
#     print(ex)
#     print('An error occurred writing to:', hex(address1))
# 
# 
# try:
#     b = bus.read_byte_data(address1, 0x80)
#     print(b)
# except Exception as ex:
#     print(ex)
#     print('An error occurred reading from:', hex(address1))
#     
# bus.close()







# Simple demo of the TCS34725 color sensor.
# Will detect the color from the sensor and print it out every second.
import time
 
import board
import busio
 
import adafruit_tcs34725
 
 
# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

sensor._write_u8(0x00, 0x10)

# Main loop reading color and printing it every second.
while True:
    sensor.interrupt = False
    print(sensor.interrupt)
    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux
    print("Temperature: {0}K Lux: {1}".format(temp, lux))
    # Delay for a second and repeat.
    sensor.interrupt = False
    time.sleep(1.0)