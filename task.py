import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)


chan_list = [24, 25, 8, 7, 12, 16, 20, 21] 

GPIO.setup(chan_list, GPIO.OUT)

for led in chan_list:
    GPIO.output(led, 0)

def lightUp(ledNumber, period):
    GPIO.output(chan_list[ledNumber], 1)
    time.sleep(period)
    GPIO.output(chan_list[ledNumber], 0)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        GPIO.output(chan_list[ledNumber], 1)
        time.sleep(blinkPeriod)
        GPIO.output(chan_list[ledNumber], 0)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    for i in range(count):
        for led in chan_list:
            GPIO.output(led, 1)
            time.sleep(period)
            GPIO.output(led, 0)

def runningDark(count,period):
    for led in chan_list:
        GPIO.output(led, 1)

    for i in range(count):
        for led in chan_list:
            GPIO.output(led, 0)
            time.sleep(period)
            GPIO.output(led, 1) 


def decToBinList(decNumber):
    bin_str = bin(decNumber)
    print(bin_str)

    result = [0, 0, 0, 0, 0, 0, 0, 0]

    c = 0
    for i in range(2, len(bin_str)):
        result[c] = int(bin_str[i])
        print(result[c])
        c = c + 1
    print(result)
    return result

def lightNumber(decNumber):
    num = decToBinList(decNumber)
    print(num)
    num.reverse()
    print(num)

    led_amount = 0
    for i in range(8):
        led_amount += num[i]

    light_led_list = list(range(led_amount))
    c = 0

    for i in range(8):
        if (num[i] == 1):
            light_led_list[c] = chan_list[i]
            c = c + 1
    print(light_led_list)
    
    GPIO.output(light_led_list, 1)
    time.sleep(3)
    GPIO.output(light_led_list, 0)

#def runningPattern(pattern, direction):


#==================================================================


num = decToBinList(1)
print(num)

lightNumber(1)

GPIO.cleanup()