import spidev 
import time 

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000

one = 0x0D
two = 0x16
three = 0x1C
four = 0x23

def write_pot(input):
    msb = 0x13
    lsb = input & 0xFF
    spi.xfer([msb,lsb])

def selection(loop):
    x = 1
    while x < 2:
        if loop == 1:
            dwell_time = int(input("Dwell time in seconds:"))
            write_pot(one)
            time.sleep(dwell_time)
            write_pot(two)
            time.sleep(dwell_time)
            write_pot(three)
            time.sleep(dwell_time)
            write_pot(four)
            time.sleep(dwell_time)
            break
        if loop == 2:
            pot_value = int(input("choose 1 (4mA), 2 (10mA), 3 (14mA), or 4 (20mA):"))
            if pot_value == 1:
                write_pot(one)
            elif pot_value == 2:
                write_pot(two)
            elif pot_value == 3:
                write_pot(three)
            elif pot_value == 4:
                write_pot(four)
        else:
            continue
        x = 1 + x

        
def question():

    loop = int(input("Type \'1\' for auto: \nType \'2\' for manual: "))
    selection(loop)
    

while True:
    question()
        
    
    # write_pot(0xFA)
    
    
    