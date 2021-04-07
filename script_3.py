import RPi.GPIO as GPIO
import time 

import numpy as np
import matplotlib.pyplot as plt
#from time import sleep

import smod

GPIO.setmode(GPIO.BCM)


ledPin=[10, 9, 11, 5, 6, 13, 19, 26]
NLed = 8 

GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, 0)

PI = 3.14

MIN = 0
MAX = 255
DELAY = 0.05

#TIME = 
#FREQUENCY = 
#samplingFrequency =

try: 

    step_time = float(1/float(samplingFrequency))

    time = np.arange(0, TIME, step_time)
    amplitude = np.sin(2 * PI * FREQUENCY * time) # sin(wt), где w = 2pi * f

    plt.plot(time, amplitude)
    plt.title('Синус')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда sin(time)')
    plt.show()
    
    print("Do you want to continue? (Y/N): ")
    ans = input()

    if (ans == 'N'):
        break
    else if (ans == 'Y'):
        for val in amplitude:
            smod.lightNumber(val)
            time.sleep(step_time)
            smod.lightNumber(0)
    else:
        print("error!")

except Exception:
    print("Found an error! :(")
else:
    print("There are no errors! :)")
finally:
    print("The end of program.")

GPIO.cleanup()