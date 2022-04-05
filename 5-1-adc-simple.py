# Cкрипт, который реализует АЦП при помощи последовательного перебора значений.

import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

# max_voltage = 3.3

# Режим обращения к GPIO
GPIO.setmode(GPIO.BCM)

# Настроили на выход все 8 GPIO-пинов  из списка dac
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

# Настроить на вход GPIO-пин comp
GPIO.setup(comp, GPIO.IN)

# Настроить на выход GPIO-пин тройка-модуля и задать значение по
# умолчанию при помощи аргумента initial
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)


# Функция перевода десятичного числа в список 0 и 1
def decimal2binary(i):
        return [int(elem) for elem in bin(i)[2:].zfill(8)]



# Функция adc() возвращает десятичное число, пропорциональное напряжению клемме S тройка-модуля
def adc(value):
    comp_value = GPIO.input(comp)
    return comp_value

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)

    return signal

try:
    while True:
        for value in range(256):
            signal = num2dac(value)
            time.sleep(0.008)
            voltage = value / 256*3.3
            comp_value = adc(value)
             
            if comp_value == 0:
                print("adc value = {:^3} -> {}, voltage = {:.2f}".format(value, signal, voltage))
                break
           
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)



