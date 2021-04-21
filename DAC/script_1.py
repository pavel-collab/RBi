import RPi.GPIO as GPIO
import time 

import smod


ledPin=[10, 9, 11, 5, 6, 13, 19, 26]
NLed = 8 

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, 0)

#==========================================================================

try:

    value = int(input('input value (-1 to exit): '))
    assert value >= 0
    assert value <= 255

    while (value != -1):
        smod.num2dac(value, ledPin)
        value = int(input('input value (-1 to exit): '))
        assert (value >= 0) | (value == -1)
        assert value <= 255

    GPIO.output(ledPin, 0)

#except Exception:
    #print("Found an error! :(")
#else:
    #print("There are no errors! :)")
finally:
    print("The end of program.")

GPIO.cleanup()