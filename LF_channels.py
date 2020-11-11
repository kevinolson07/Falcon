import spidev 
import time 
import RPi.GPIO as GPIO

channel_1 = 16
channel_2 = 18

# Hex values for equivalant resistance
one = 0x0D
two = 0x16
three = 0x1C
four = 0x23

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel_1,GPIO.OUT)
GPIO.setup(channel_2,GPIO.OUT)
GPIO.output(channel_1, GPIO.HIGH)
GPIO.output(channel_2, GPIO.HIGH)
                                                                                                                                                                        
def write_pot(input):
    msb = 0x13
    lsb = input & 0xFF
    spi.xfer([msb,lsb])

def selection(loop, channel_select):
    x = 1
    while x <= 1:
        if loop == 1:
            try:
                dwell_time = int(input("Dwell time in seconds:"))
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(one)
                GPIO.output(channel_select, GPIO.HIGH)
                time.sleep(dwell_time)
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(two)
                GPIO.output(channel_select, GPIO.HIGH)
                time.sleep(dwell_time)
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(three)
                GPIO.output(channel_select, GPIO.HIGH)
                time.sleep(dwell_time)
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(four)
                GPIO.output(channel_select, GPIO.HIGH)
                time.sleep(dwell_time)
                print("completed auto")
                x+=1
            except ValueError:
                print("Invalid Value")
                question1()
        if loop == 2:
            pot_value = int(input("choose 1 (4mA), 2 (10mA), 3 (14mA), or 4 (20mA):"))
            if pot_value == 1:
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(one)
                GPIO.output(channel_select, GPIO.HIGH)
                x+=1
            elif pot_value == 2:
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(two)
                GPIO.output(channel_select, GPIO.HIGH)
                x+=1
            elif pot_value == 3:
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(three)
                GPIO.output(channel_select, GPIO.HIGH)
                x+=1
            elif pot_value == 4:
                GPIO.output(channel_select, GPIO.LOW)
                write_pot(four)
                GPIO.output(channel_select, GPIO.HIGH)
                x+=1
            else:
                print("Invalid Value")
                question1()
        else:
            question1()

        
def question(channel_select):
    x = 1
    while x <= 1:
        try:
            loop = int(input("Type \'1\' for auto: \nType \'2\' for manual: "))
            if loop == 1 and channel_select == 1:
                x+=1
                selection(loop, channel_1)
            if loop == 2 and channel_select == 1:
                x+=1
                selection(loop, channel_1)
            if loop == 1 and channel_select == 2:
                x+=1
                selection(loop, channel_2)
            if loop == 2 and channel_select == 2:
                x+=1
                selection(loop, channel_2)
            else:
                print("Try again")
        except ValueError:
            print("Invalid Value")

def question1():
    i=1
    while i <= 1:
        try:
            channel_select = int(input("Channel 1 or 2?"))
            if channel_select == 1 or channel_select == 2:
                i+=1
                question(channel_select)
            else:
                print("sorry, try again ")
        except ValueError:
            print("Invalid Value")
    

while True:
    question1()
   
    
    # write_pot(0xFA)
    
    
    