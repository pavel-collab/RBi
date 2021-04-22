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

    while True:
        for value in range(0, 255):
            smod.num2dac(value, ledPin)
            time.sleep(0.001)
            if GPIO.input(4) == 0:
                print("value: ", value, " V = ", (value/255) * 3.3)
                break

#except Exception:
    #print("Found an error! :(")
#else:
    #print("There are no errors! :)")
finally:
    print("The end of program.")
    GPIO.cleanup()