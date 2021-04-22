import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)


chan_list = [24, 25, 8, 7, 12, 16, 20, 21] 
ledPin=[10, 9, 11, 5, 6, 13, 19, 26]

NLed = 8 

GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(chan_list, 0)

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, 0)

# зажигает светодиод номер ledNumber из списка D_list на время period
def lightUp(ledNumber, period, D_list):
    GPIO.output(D_list[ledNumber], 1)
    time.sleep(period)
    GPIO.output(D_list[ledNumber], 0)

# мигает светодиодом номер ledNumber из списка D_list, blinkCount раз с периодом blinkPeriod
def blink(ledNumber, blinkCount, blinkPeriod, D_list):
    for i in range(blinkCount):
        GPIO.output(D_list[ledNumber], 1)
        time.sleep(blinkPeriod)
        GPIO.output(D_list[ledNumber], 0)
        time.sleep(blinkPeriod)

# зажигает по порядку один светодиод за другим count раз (светодиод горит period секудн)
# D_list -- список используемых диодов
def runningLight(count, period, D_list):
    for i in range(count):
        for led in D_list:
            GPIO.output(led, 1)
            time.sleep(period)
            GPIO.output(led, 0)

# гасит по порядку один светодиод за другим count раз (светодиод не горит period секудн)
# D_list -- список используемых диодов
def runningDark(count, period, D_list):
    for led in D_list:
        GPIO.output(led, 1)

    for i in range(count):
        for led in D_list:
            GPIO.output(led, 0)
            time.sleep(period)
            GPIO.output(led, 1) 


#---------------------------------------------------------------

# переводит число dec_num из десятичной системы в двоичную, возвращает список длиной 8
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

# зажигает светодиодами узор, соответствующий представлению числа decNum в двоичной системе
# D_list -- список используемых диодов
def lightNumber(decNumber, delay_time, D_list):
    num = decToBinList(decNumber)
    num.reverse()
    index_list = []

    for i in range(len(num)):
        if (num[i] == 1):
            index_list.append(i)

    light_led_list = [D_list[index] for index in index_list]
    
    GPIO.output(light_led_list, 1)
    time.sleep(delay_time)
    GPIO.output(light_led_list, 0)

# зажигает светодиодами узор, соответствующий представлению числа decNum в двоичной системе
# D_list -- список используемых диодов
def num2dac(value, D_list):
    GPIO.output(D_list, 0)
    num = decToBinList(value)
    num.reverse()
    index_list = []

    for i in range(len(num)):
        if (num[i] == 1):
            index_list.append(i)

    light_led_list = [D_list[index] for index in index_list]
    
    GPIO.output(light_led_list, 1)


# циклично сдвигает "узор", соответсвующий числу pattern в двоичном представлении
# смещение узора происходит влево или вправо в зависимости от direction
def runningPattern(pattern, direction):
    num = decToBinList(pattern)
    num.reverse()
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

# =-_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_-

# контроль яркости светодиода номер ledNumber спомощью ШИМ
def PWM_light_control(ledNumber):
    GPIO_PWM_0 = chan_list[ledNumber]                   # рабочий канал
    FREQUENCY = 45                                      # частота
    DELAY_TIME = 0.01                                   # время задержки
    
    pwmOutput_0 = GPIO.PWM(GPIO_PWM_0, FREQUENCY)       # создаем объект для работы с каналом PWM
    pwmOutput_0.start(0)                                # начальный коэффициент заполнения 0
    
    
    try:
        while True:
            for dutyCycle in range(0, 101, 1):
                #print("up")
                pwmOutput_0.ChangeDutyCycle(dutyCycle)  # меняем коэффициент заполнения
                time.sleep(DELAY_TIME) 
            for dutyCycle in range(100, -1, -1):
                #print("down")
                pwmOutput_0.ChangeDutyCycle(dutyCycle)
                time.sleep(DELAY_TIME)
    except KeyboardInterrupt:
        pwmOutput_0.stop()                              # прерывание: ctrl + C

# =-_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_--_-_-

GPIO.cleanup()