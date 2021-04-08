import RPi.GPIO as GPIO
from time import sleep

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

TIME = 2
FREQUENCY = 2  
samplingFrequency = 1000

try: 

    step_time = float(1/float(samplingFrequency))

    time = np.arange(0, TIME, step_time)
    amplitude = 0.5 * (1 + np.sin(2 * PI * FREQUENCY * time)) # sin(wt), где w = 2pi * f

    plt.plot(time, amplitude)
    plt.title('Синус')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда sin(time)')
    plt.show()
    
    print("Do you want to continue? (Y/N): ")
    ans = input()

    if (ans == 'N'):
        print("Exit!")
    elif (ans == 'Y'):
        for val in amplitude:
            smod.lightNumber(int(val * 255), step_time)
    else:
        print("error!")

finally:
    print("The end of program.")

GPIO.cleanup()

