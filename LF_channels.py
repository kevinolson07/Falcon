import spidev 
import time 
import RPi.GPIO as GPIO

channel_1 = 16
channel_2 = 18
channel_3 = 22
channel_4 = 36
all_channels = (16,18,22,36)

# Hex values for equivalant resistance
one = 0x10      #625 Ohms
two = 0x16      #910 Ohms
three = 0x1C        #1150 Ohms 
four = 0x20     #1385 Ohms
bank_1 = 0x11
bank_2 = 0x12
all_banks = 0x13

spi = spidev.SpiDev()
spi.max_speed_hz = 976000
GPIO.setmode(GPIO.BOARD)
GPIO.setup(all_channels,GPIO.OUT)
GPIO.output(all_channels, GPIO.HIGH)
                                                                                                                                                                        
def write_pot(input,bank_select):
    spi.open(0,0)
    msb = bank_select
    lsb = input & 0xFF
    spi.xfer([msb,lsb])
    spi.close()

def settings(channel_select, mode, bank_select):
    x = 1
    while x <= 1:
        if mode == 1:
            dwell_time = int(input("Dwell time in seconds:"))
            cycles = int(input("Enter number of cycles:"))
            try:
                for c in range(cycles):
                    bank_select = all_banks
                    print(channel_select, mode)
                    GPIO.output(all_channels, GPIO.LOW)
                    write_pot(one,all_banks)
                    GPIO.output(all_channels, GPIO.HIGH)
                    time.sleep(dwell_time)
                    GPIO.output(all_channels, GPIO.LOW)
                    write_pot(two,all_banks)
                    GPIO.output(all_channels, GPIO.HIGH)
                    time.sleep(dwell_time)
                    GPIO.output(all_channels, GPIO.LOW)
                    write_pot(three,all_banks)
                    GPIO.output(all_channels, GPIO.HIGH)
                    time.sleep(dwell_time)
                    GPIO.output(all_channels, GPIO.LOW)
                    write_pot(four,all_banks)
                    GPIO.output(all_channels, GPIO.HIGH)
                    time.sleep(dwell_time)
                    print("completed auto")
                    x+=1
            except ValueError:
                print("Invalid Value combination")
                # mode_select()
        if mode == 2:
            pot_value = int(input("Choose 1 (4mA), 2 (10mA), 3 (14mA), or 4 (20mA):"))
            if pot_value == 1:
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(one, bank_select)
                GPIO.output(channel_select, GPIO.HIGH)
                x+=1
            elif pot_value == 2:
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(two, bank_select)
                GPIO.output(channel_select, GPIO.HIGH)
                x+=1
            elif pot_value == 3:
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(three, bank_select)
                GPIO.output(channel_select, GPIO.HIGH)
                x+=1
            elif pot_value == 4:
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(four, bank_select)
                GPIO.output(channel_select, GPIO.HIGH)
                x+=1
            else:
                print("Invalid Value")
        # else:
        #     mode_select()

        
def mode_select():
    x = 1
    while x <= 1:
        try:
            mode = int(input("Type \'1\' for auto or \'2\' for manual: "))
            if mode == 1:
                x+=1
                settings(None, mode, None)
            elif mode == 2:
                x+=1
                channel_select(mode)
            else:
                print("Try again")
        except ValueError:
            print("Invalid Value")

def channel_select(mode):
    i=1
    while i <= 1:
        try:
            channel_select = int(input("Type \'1\' for channel 1 or \'2\' for channel 2 or \'3\' for channel 3 or \'4\' for channel 4: "))
            bank_select = int(input("Type \'1\' for bank 1 or \'2\' for bank 2: "))
            if channel_select == 1 and bank_select ==1:
                channel_select = channel_1
                bank_select = bank_1
                i+=1
                settings(channel_select,mode, bank_select)

            elif channel_select == 1 and bank_select == 2:
                channel_select = channel_1
                bank_select = bank_2
                i+=1
                settings(channel_select,mode,bank_select)

            elif channel_select == 2 and bank_select == 1:
                channel_select = channel_2
                bank_select = bank_1
                i+=1
                settings(channel_select,mode,bank_select)

            elif channel_select == 2 and bank_select == 2:
                channel_select = channel_2
                bank_select = bank_2
                i+=1
                settings(channel_select,mode,bank_select)
            elif channel_select == 3 and bank_select == 1:
                channel_select = channel_3
                bank_select = bank_1
                i+=1
                settings(channel_select,mode,bank_select)

            elif channel_select == 3 and bank_select == 2:
                channel_select = channel_3
                bank_select = bank_2
                i+=1
                settings(channel_select,mode,bank_select)
            elif channel_select == 4 and bank_select == 1:
                channel_select = channel_4
                bank_select = bank_1
                i+=1
                settings(channel_select,mode,bank_select)

            elif channel_select == 4 and bank_select == 2:
                channel_select = channel_4
                bank_select = bank_2
                i+=1
                settings(channel_select,mode,bank_select)

            else:
                print("Bad combination, try again ")
        except ValueError:
            print("Invalid Value")
    

while True:
    mode_select()
   
    
    # write_pot(0xFA)
    
    
    