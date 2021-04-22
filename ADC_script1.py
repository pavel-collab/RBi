import RPi.GPIO as GPIO
import time 

import smod
GPIO.setmode(GPIO.BCM)

ledPin=[10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, 0)

CMP = 4
SIG = 17

GPIO.setup(SIG, GPIO.OUT) # устанавливаем пин cmp, как выход
GPIO.setup(CMP, GPIO.IN)  # устанавливаем пин как вход

try:

    value = int(input('Enter value (-1 to exit): '))
    assert value >= 0
    #assert value <= 255

    while (value != -1):
        smod.num2dac(value, ledPin)
        time.sleep(0.01)
        print("value: ", value, " V = ", (value/255) * 3.3)

        value = int(input('Enter value (-1 to exit): '))
        assert (value >= 0) | (value == -1)
        assert value <= 255

#except Exception:
    #print("Found an error! :(")
#else:
    #print("There are no errors! :)")
finally:
    print("The end of program.")

GPIO.cleanup()