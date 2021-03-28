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


#---------------------------------------------------------------

# first vesion
'''def decToBinList(dec_num):
    bin_str = bin(dec_num)

    bin_str_list = list(bin_str)[2::]

    result = []
    for num in bin_str_list:
        result.append(int(num))

    return result'''

# second version
'''def decToBinList(dec_num):
    result = []

    while(True):

        frac = dec_num % 2
        main = dec_num // 2

        result.append(frac)
        dec_num = dec_num // 2

        if ((main) == 0):
            break

    result.reverse()

    return result'''

# first version (format output)
'''def decToBinList(dec_num):
    bin_str = bin(dec_num)
    
    bin_str_list = list(bin_str)[2::]

    result = []
    for num in bin_str_list:
        result.append(int(num))

    if (len(result) < 8):
        for i in range(8 - len(result)):
            result = [0] + result

    return result'''

# second version (format output)
def decToBinList(dec_num):
    result = []

    while(True):

        frac = dec_num % 2
        main = dec_num // 2

        result.append(frac)
        dec_num = dec_num // 2

        if ((main) == 0):
            break

    result.reverse()

    if (len(result) < 8):
        for i in range(8 - len(result)):
            result = [0] + result

    return result

#---------------------------------------------------------------

def lightNumber(decNumber):
    num = decToBinList(decNumber)
    index_list = []

    for i in range(len(num)):
        if (num[i] == 1):
            index_list.append(i)

    light_led_list = [chan_list[index] for index in index_list]
    
    GPIO.output(light_led_list, 1)
    time.sleep(3)
    GPIO.output(light_led_list, 0)

def runningPattern(pattern, direction):
    num = decToBinList(pattern)
    index_list = []

    for i in range(9):
        for i in range(len(num)):
            if (num[i] == 1):
                index_list.append(i)

        light_led_list = [chan_list[index] for index in index_list]
    
        GPIO.output(light_led_list, 1)
        time.sleep(0.5)
        GPIO.output(light_led_list, 0)
        
        if (direction == 'left'):
            num = num[1:] + num[:1]
        elif (direction == 'right'):
            num = num[-1:] + num[:-1]
            
        index_list = []

#==================================================================



GPIO.cleanup()