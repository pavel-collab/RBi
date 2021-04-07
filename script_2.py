import RPi.GPIO as GPIO
import time 

import smod

GPIO.setmode(GPIO.BCM)


ledPin=[10, 9, 11, 5, 6, 13, 19, 26]
NLed = 8 

GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, 0)

MIN = 0
MAX = 255
DELAY = 0.05 

try:

    repetitionsNumber = int(input("number of repetitions: "))
    assert repetitionsNumber > 0

    for i in range (0, repetitionsNumber):
        for j in range(MIN, MAX):
            smod.lightNumber(MIN + j)
            time.sleep(DELAY)
            smod.lightNumber(0)
        for j in range (MIN, MAX):
            smod.lightNumber(MAX - j)
            time.sleep(DELAY)
            smod.lightNumber(0)

except Exception:
    print("Found an error! :(")
else:
    print("There are no errors! :)")
finally:
    print("The end of program.")

GPIO.cleanup()