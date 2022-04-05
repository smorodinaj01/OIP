import RPi.GPIO as GPIO
import time

# Треугольный сигнал


GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
clean_bin = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup (dac, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

# В блоке try создать бесконечный цикл, 
# формирующий треугольный аналоговый сигнал на выходе ЦАП

try:
    num = 0
    up = 1
    print("Period:")
    period = int (input())
    ps = period / (256 * 2)

    while (1):
        time.sleep(ps)
        binary = dec2bin(num)
        GPIO.output(dac, binary)

        if num == 255:
            up = -1
        if num == 0:
            up = 1
        num += up

# В блоке finally подать 0 на все пины dac и очистить настройки GPIO        
finally:
    GPIO.output (dac, clean_bin)
    GPIO.cleanup ()