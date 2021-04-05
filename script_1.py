import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)


ledPin=[10, 9, 11, 5, 6, 13, 19, 26]
NLed = 8 

GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, 0)

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

def num2dac(value):
    num = decToBinList(value)
    index_list = []

    for i in range(len(num)):
        if (num[i] == 1):
            index_list.append(i)

    light_led_list = [ledPin[index] for index in index_list]
    
    GPIO.output(light_led_list, 1)
    time.sleep(3)
    GPIO.output(light_led_list, 0)

#==========================================================================

try:

    value = int(input('input value (-1 to exit: )'))

    while (value != -1):
        num2dac(value)
        value = int(input('input value (-1 to exit: )'))

except Exception:
    print("Found an error! :(")
else:
    print("There are no errors! :)")
finally:
    print("The end of program.")

GPIO.cleanup()