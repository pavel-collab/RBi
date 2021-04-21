import RPi.GPIO as GPIO
import time 

import smod

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, 0)

# change chan_list to ledList

ledPin=[10, 9, 11, 5, 6, 13, 19, 26]
NLed = 8 

MIN = 0
MAX = 255
DELAY = 0.05 

try:

    repetitionsNumber = int(input("input number of repetitions: "))
    assert repetitionsNumber > 0

    for i in range (0, repetitionsNumber):
        for j in range(MIN, MAX):
            smod.lightNumber(MIN + j, ledPin)
            #time.sleep(DELAY)
            #smod.lightNumber(0)
        for j in range (MIN, MAX):
            smod.lightNumber(MAX - j, ledPin)
            #time.sleep(DELAY)
            #smod.lightNumber(0)
finally:
    print("The end of program.")
    GPIO.output(ledPin, 0)

GPIO.cleanup()