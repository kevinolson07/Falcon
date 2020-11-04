import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.output(17,GPIO.LOW)

# max_freq = 20
# min_freq = 1
duty = .5




def pwm(freq,liftoff_freq, touchdown_freq):
    for x in range(freq):
        if freq >= liftoff_freq and freq <= touchdown_freq:
             GPIO.output(17,GPIO.HIGH)
        else:
            GPIO.output(18,GPIO.LOW)
        delay = (1/freq)*.5
        GPIO.output(18,GPIO.HIGH)
        print("HIGH")
        time.sleep(delay)
        GPIO.output(18,GPIO.LOW)
        print("LOW")
        time.sleep(delay)


try:   
    min_freq = int(input("Enter min frequency:"))
except ValueError:
    print("Value you entered is not of value int.")
    min_freq = int(input("Enter min frequency:"))

try:   
    max_freq = int(input("Enter max frequency:"))
except ValueError:
    print("Value you entered is not of value int.")
    max_freq = int(input("Enter max frequency:"))

try:   
    liftoff_freq = int(input("Enter liftoff frequency:"))
except ValueError:
    print("Value you entered is not of value int.")
    liftoff_freq = int(input("Enter min frequency:"))

try:   
    touchdown_freq = int(input("Enter touchdown frequency:"))
except ValueError:
    print("Value you entered is not of value int.")
    touchdown_freq = int(input("Enter touchdown frequency:"))


for i in range(min_freq,max_freq):
    pwm(i,liftoff_freq, touchdown_freq)