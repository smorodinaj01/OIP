# При помощи алгоритма АЦП отобразить величину напряжения в области leds.

import RPi.GPIO as GPIO
import time


# Режим обращения к GPIO
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

bin = [1, 0, 0, 0, 0, 0, 0, 0]
comp = 4
troyka = 17

max = 3.3
bits = 8
levels = 2**bits
voltage = 0

# Настройка на выход всех 8 GPIO-пинов
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)

# Настроить на выход GPIO-пин тройка-модуля и задать значение по
# умолчанию при помощи аргумента initial
GPIO.setup(troyka, GPIO.OUT, initial = 1)

# Настроить на вход GPIO-пин comp
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    bin = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (bits):
        bin[i] = 1
        GPIO.output(dac, bin)
        time.sleep(0.1)
        value = GPIO.input(comp)
        if value == 0:
            bin[i] = 0
        else:
            bin[i] = 1
    return bin[0] * 128 + bin[1]*64 + bin[2]*32 + bin[3]*16 + bin[4]*8 + bin[5]*4 + bin[6]*2 + bin[7]

# в блоке try:
# в бесконечном цикле вызывать функцию adc()
# преобразовать возвращаемое значение и выдать его на leds при помощи функции c прошлого занятия

try:
    while True:
        voltage = adc()
        print('voltage is {:.2f}'.format(voltage*max/levels, voltage))
        num = round(bits/levels*voltage)
        print(num)
        GPIO.output(leds, decimal2binary(2**num-1))
        time.sleep(0.1)

except KeyboardInterrupt:   # Ошибка
    print('/nStop')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()