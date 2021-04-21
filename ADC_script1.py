import RPi.GPIO as GPIO
import time 

import smod

DAC = 
SIG = 

GPIO.setup(DAC, GPIO.OUT) # устанавливаем пин DAC, как выход
GPIO.setup(SIG, GPIO.IN)  # устанавливаем пин SIG, как вход

try:

    value = int(input('Enter value (-1 to exit): '))
    assert value >= 0
    assert value <= 255

    while (value != -1):
        if ():
            #smod.num2dac(value, ledPin)
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