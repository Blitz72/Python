import smbus
from time import sleep

channel = 1
address1 = 0x24
address2 = 0x25
IODIRA = 0x00
IODIRB = 0x01
GPIOA = 0x12
GPIOB = 0x13

time_delay = 0.5

try:
   bus = smbus.SMBus(channel)
except Exception as ex:
    print(ex)
    print("Failed to initialize i2c bus.")

try:
    bus.write_byte_data(address1, IODIRA, 0x00)
    bus.write_byte_data(address1, IODIRB, 0x00)
except Exception as ex:
    print(ex)
    print('An error occurred writing to:', hex(address1))
try:
    bus.write_byte_data(address2, IODIRA, 0x00)
    bus.write_byte_data(address2, IODIRB, 0x00)
except Exception as ex:
    print(ex)
    print('An error occurred writing to:', hex(address2))


# turn off all relays
def clear_outputs():
    bus.write_byte_data(address1, GPIOA, 0x00)
    bus.write_byte_data(address1, GPIOB, 0x00)
    bus.write_byte_data(address2, GPIOA, 0x00)


# turn on all relays
def all_outputs_on():
    bus.write_byte_data(address1, GPIOA, 0xff)
    bus.write_byte_data(address1, GPIOB, 0xff)
    bus.write_byte_data(address2, GPIOA, 0x07)


# for early testing of MCP23017 boards, not to be used when testing individual 120VAC loads
def cycle_outputs():
    
    for y in range(10):
        for x in range(8):
            bus.write_byte_data(address1, GPIOA, 1<<x)
            sleep(time_delay)
        bus.write_byte_data(address1, GPIOA, 0)
        for x in range(8):
            bus.write_byte_data(address1, GPIOB, 1<<x)
            sleep(time_delay)
        bus.write_byte_data(address1, GPIOB, 0)
        for x in range(8):
            bus.write_byte_data(address2, GPIOA, 1<<x)
            sleep(time_delay)
        bus.write_byte_data(address2, GPIOA, 0)


# reset all devices in bay using V2 sequence
def reset_all():
    
    clear_outputs()
    sleep(5)
    for x in range(5):
        all_outputs_on()
        sleep(8)
        clear_outputs()
        sleep(2)
    all_outputs_on()
    

# b = bus.read_byte_data(address2, GPIOA)
# print(b)
# print(~b & 0xff)


# reset an individual relay
def reset_relay(relay_num):
    
    # test to see if valid relay number, then assign proper address and GPIO register
    if not 1 <= relay_num <= 19:
        print('Please enter a relay number between 1 and 19')
        return
    if 1 <= relay_num <= 8:
        address = 0x24
        gpio_reg = GPIOA
    elif 9 <= relay_num <= 16:
        address = 0x24
        gpio_reg = GPIOB
    else:
        address = 0x25
        gpio_reg = GPIOA
        
    # see what's already in ON/OFF in the register
    b = bus.read_byte_data(address, gpio_reg)
    print('GPIO register: ', b)
    
    # generate a bitmask for turning the relay off with bitwise &
    bitmask = ~(1 << ((relay_num - 1) % 8)) & 0xff
    print('bitmask: ', bitmask)
    
    # turn the relay off for 5 seconds
    bus.write_byte_data(address, gpio_reg, b & bitmask)
    sleep(5)
    for x in range(5):
        bus.write_byte_data(address, gpio_reg, (1 << ((relay_num - 1) % 8)) | b)
        sleep(8)
        bus.write_byte_data(address, gpio_reg, b & bitmask)
        sleep(2)
    
    # finally turn the relay on after the reset sequence
    bus.write_byte_data(address, gpio_reg, (1 << ((relay_num - 1) % 8)) | b)


# toggle an individual relay by wire number
def toggle_relay(relay_num):
    
    # test to see if valid relay number, then assign proper address and GPIO register
    if not 1 <= relay_num <= 19:
        print('Please enter a relay number between 1 and 19')
        return
    if 1 <= relay_num <= 8:
        address = 0x24
        gpio_reg = GPIOA
    elif 9 <= relay_num <= 16:
        address = 0x24
        gpio_reg = GPIOB
    else:
        address = 0x25
        gpio_reg = GPIOA
    
    # see what's already in ON/OFF in the register
    b = bus.read_byte_data(address, gpio_reg)
    print('GPIO register: ', b)
    
    # generate a bitmask for turning the relay off with bitwise &
    bitmask = ~(1 << ((relay_num - 1) % 8)) & 0xff
    print('bitmask: ', bitmask)
    
    # test to see if the relay is already on
    if (1 << ((relay_num - 1) % 8)) & b:
        print('Relay is ON! Turning it OFF!')
        bus.write_byte_data(address, gpio_reg, b & bitmask)
    else:
        print('Relay is OFF! Turning it ON!')
        bus.write_byte_data(address, gpio_reg, (1 << ((relay_num - 1) % 8)) | b)


# toggle_relay(16)
#all_outputs_on()
#reset_relay(19)
#all_outputs_on()
#sleep(15)
#reset_all()
# clear_outputs()
# cycle_outputs()
