import smbus
from time import sleep

CHANNEL = 1
IO_ADDRESS1 = 0x24  # i2c address of first MCP23017
IO_ADDRESS2 = 0x25  # i2c address of second MCP23017
# MUX_ADDRESS1 = 0x70
# MUX_ADDRESS2 = 0x71
# MUX_ADDRESS3 = 0x72
# SENSOR_ADDRESS = 0x29
IO_IODIRA = 0x00    # address of I/O direction register for PORT A
IO_IODIRB = 0x01    # address of I/O direction register for PORT B 
IO_GPIOA = 0x12     # address of GPIO PORT A register 
IO_GPIOB = 0x13     # address of GPIO PORT B register


# assign configuration varaibles based on relay number
def get_config(relay_num):
    """Get the i2c address and corresponding GPIO register based on the relay number.

    Inputs: relay_num, must be an integer 1 to 19 inclusive.
    Returns: address, gpio_reg
    """
    if 1 <= relay_num <= 8:
        address = 0x24
        gpio_reg = IO_GPIOA
    elif 9 <= relay_num <= 16:
        address = 0x24
        gpio_reg = IO_GPIOB
    elif 17 <= relay_num <= 19:
        address = 0x25
        gpio_reg = IO_GPIOA
    else:
        raise ValueError('Please enter a value between 1 and 19')

    return address, gpio_reg


# turn off all relays
def clear_outputs():
    """Turn off all relays."""
    bus.write_byte_data(IO_ADDRESS1, IO_GPIOA, 0x00)
    bus.write_byte_data(IO_ADDRESS1, IO_GPIOB, 0x00)
    bus.write_byte_data(IO_ADDRESS2, IO_GPIOA, 0x00)


# turn on all relays
def all_outputs_on():
    """Turn on all relays."""
    bus.write_byte_data(IO_ADDRESS1, IO_GPIOA, 0xff)
    bus.write_byte_data(IO_ADDRESS1, IO_GPIOB, 0xff)
    bus.write_byte_data(IO_ADDRESS2, IO_GPIOA, 0x07)


# for early testing of MCP23017 boards, not to be used when testing individual 120VAC loads
def cycle_outputs(time_delay=10, iterations=1):
    
    for y in range(iterations):
        for x in range(8):
            bus.write_byte_data(IO_ADDRESS1, IO_GPIOA, 1<<x)
            sleep(time_delay)
        bus.write_byte_data(IO_ADDRESS1, IO_GPIOA, 0)
        for x in range(8):
            bus.write_byte_data(IO_ADDRESS1, IO_GPIOB, 1<<x)
            sleep(time_delay)
        bus.write_byte_data(IO_ADDRESS1, IO_GPIOB, 0)
        for x in range(8):
            bus.write_byte_data(IO_ADDRESS2, IO_GPIOA, 1<<x)
            sleep(time_delay)
        bus.write_byte_data(IO_ADDRESS2, IO_GPIOA, 0)


# reset all devices in bay using V2 sequence
def reset_all():
    """Reset all devices in the bay using the C by GE V2 sequence."""
    clear_outputs()
    sleep(5)
    for x in range(5):
        all_outputs_on()
        sleep(8)
        clear_outputs()
        sleep(2)
    all_outputs_on()
    

# b = bus.read_byte_data(IO_ADDRESS2, IO_GPIOA)
# print(b)
# print(~b & 0xff)


# reset an individual relay
def reset_relay(relay_num):
    """Reset individual relay using the C by GE V2 sequence.

    Inputs: relay_num, must be an integer between 1 and 19 inclusive.
    """
    address, gpio_reg = get_config(relay_num)
        
    # see if the relay is already ON/OFF in the GPIOx register
    b = bus.read_byte_data(address, gpio_reg)
#     print('i2c address:    ', hex(address))
#     print('GPIO reg value: ', hex(b))
    
    # generate a bitmask for turning the relay off with bitwise &
    bitmask = ~(1 << ((relay_num - 1) % 8)) & 0xff
#     print('bitmask: ', bitmask)
    
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


def relay_on(relay_num):
    """Turn on an individual relay.

    Inputs: relay_num, must be an integer between 1 and 19 inclusive.
    """
    address, gpio_reg = get_config(relay_num)
    print(hex(address), hex(gpio_reg))

    # see what's already in ON/OFF in the register
    b = bus.read_byte_data(address, gpio_reg)
    print('i2c address:    ', hex(address))
    print('GPIO reg vlaue: ', hex(b))

    # generate a bitmask for turning the relay off with bitwise &
    bitmask = ~(1 << ((relay_num - 1) % 8)) & 0xff
    print('bitmask: ', bitmask)

    # write new value to the proper GPIO address
    bus.write_byte_data(address, gpio_reg, (1 << ((relay_num - 1) % 8)) | b)


def relay_off(relay_num):
    """Toggle an individual relay.

    Inputs: relay_num, must be an integer between 1 and 19 inclusive.
    """
    address, gpio_reg = get_config(relay_num)
    print(hex(address), hex(gpio_reg))
    
    # see what's already in ON/OFF in the register
    b = bus.read_byte_data(address, gpio_reg)
    print('i2c address:    ', hex(address))
    print('GPIO reg vlaue: ', hex(b))
    
    # generate a bitmask for turning the relay off with bitwise &
    bitmask = ~(1 << ((relay_num - 1) % 8)) & 0xff
    print('bitmask: ', bitmask)

    # write new value to the proper GPIO address
    bus.write_byte_data(address, gpio_reg, b & bitmask)


def power_cycle(relay_num):
    """Power cycle a specific relay."""
    relay_off(relay_num)
    sleep(2)
    relay_on(relay_num)


# toggle an individual relay by wire number
def toggle_relay(relay_num):
    """Toggle an individual relay.

    Inputs: relay_num, must be an integer between 1 and 19 inclusive.
    """
    address, gpio_reg = get_config(relay_num)
#     print(hex(address), hex(gpio_reg))
    
    # see what's already in ON/OFF in the register
    b = bus.read_byte_data(address, gpio_reg)
#     print('i2c address:    ', hex(address))
#     print('GPIO reg vlaue: ', hex(b))
    
    # generate a bitmask for turning the relay off with bitwise &
    bitmask = ~(1 << ((relay_num - 1) % 8)) & 0xff
#     print('bitmask: ', bitmask)
    
    # test to see if the relay is already on
    if (1 << ((relay_num - 1) % 8)) & b:
        print('Relay is ON! Turning it OFF!')
        bus.write_byte_data(address, gpio_reg, b & bitmask)
    else:
        print('Relay is OFF! Turning it ON!')
        bus.write_byte_data(address, gpio_reg, (1 << ((relay_num - 1) % 8)) | b)


# initialize i2c bus
try:
   bus = smbus.SMBus(CHANNEL)
except Exception as ex:
    print(ex)
    print("Failed to initialize i2c bus.")


# POR (power on reset) values of IO_IODIRA and IO_IODIRB are 0xFF,
# if bit(n) of IODIRX is 1 it is input, if 0 it is an output,
# so must write 0x00 to configure the GPIO registers as outputs
try:
    bus.write_byte_data(IO_ADDRESS1, IO_IODIRA, 0x00)  # declare PORT A as outputs
    bus.write_byte_data(IO_ADDRESS1, IO_IODIRB, 0x00)  # declare PORT B as outputs
except Exception as ex:
    print(ex)
    print('An error occurred writing to:', hex(IO_ADDRESS1))
try:
    bus.write_byte_data(IO_ADDRESS2, IO_IODIRA, 0x00)  # declare PORT A as outputs
    bus.write_byte_data(IO_ADDRESS2, IO_IODIRB, 0xff)  # declare PORT B as inputs
except Exception as ex:
    print(ex)
    print('An error occurred writing to:', hex(IO_ADDRESS2))


# toggle_relay(16)
# all_outputs_on()
# reset_relay(19)
# all_outputs_on()
# reset_all()
# clear_outputs()
# cycle_outputs()