import RPi.GPIO as GPIO
import time 

import smod
#GPIO.setwarnings(False)
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
        start = 0
        end = 256
        mean = 0
        while (end - start > 2):
            mean = int((end + start) / 2)
            smod.num2dac(mean, ledPin)
            time.sleep(0.001)
            if (GPIO.input(4) == 1):
                start = mean
            else:
                end = mean
        mean = int((end + start) / 2)
        print("value: ", mean, " V = ", (mean/255) * 3.3)
            
except Exception:
    print("Found an error! :(")
#else:
    #print("There are no errors! :)")
finally:
    print("The end of program.")
    GPIO.cleanup()