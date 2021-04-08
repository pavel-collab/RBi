import smod

import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)


chan_list = [24, 25, 8, 7, 12, 16, 20, 21] 

GPIO.setup(chan_list, GPIO.OUT)

GPIO.output(chan_list, 0)

#smod.lightNumber(7)
#smod.runningPattern(7, 'left')
smod.PWM_light_control(3)

GPIO.cleanup()