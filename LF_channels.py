import spidev 
import time 

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000

one = 0x40
two = 0xA0
three = 0xFA

def write_pot(input):
    msb = 0x13
    lsb = input & 0xFF
    spi.xfer([msb,lsb])
    

while True:
    pot_value = int(input("choose 1, 2, or 3:"))
    # write_pot(0xFA)
    
    if pot_value == 1:
        write_pot(one)
    elif pot_value == 2:
        write_pot(two)
    elif pot_value == 3:
        write_pot(three)
    else:
        write_pot(0x00)