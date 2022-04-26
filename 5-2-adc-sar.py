import RPi.GPIO as GPIO
import time

dac  = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

maxVoltage = 3.3
troyka = 17
comp = 4

# Режим обращения к GPIO
GPIO.setmode(GPIO.BCM)

# Настроили на выход все 8 GPIO-пинов  из списка dac
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)

# Настроить на выход GPIO-пин тройка-модуля и задать значение по
# умолчанию при помощи аргумента initial
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

# Настроить на вход GPIO-пин comp
GPIO.setup(comp, GPIO.IN)

# Функция перевода десятичного числа в список 0 и 1
def decimal2binary(i):
        return [int(elem) for elem in bin(i)[2:].zfill(8)]

def bin2dac(i):
        signal = decimal2binary(i)
        GPIO.output(dac, signal)


# Функция adc() возвращает десятичное число, 
# пропорциональное напряжению клемме S тройка-модуля
def adc(i, value):
    if i == -1:
        return value

    bin2dac(value + 2**i)
    time.sleep(0.01)
    comp_value = GPIO.input(comp)
    if comp_value == 0:
        return adc(i-1, value)
    else:
        return adc(i-1, value + 2**i)

try:
    while True:
        const = adc(7, 0)
        print("Цифровое значение =")
        print(const)
        print("Напряжение")
        val_to_pr = const/ 2**8 * 3.3
        print(valToPr)
        val_to_pr = val_to_pr/3.3 * 8 + 0.4

        for i in range(8):
            if val_to_pr >= 1:
                GPIO.output(leds[7-i],1)
            else:
                GPIO.output(leds[7-i],0)
            val_to_pr = val_to_pr - 1
            
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.cleanup(leds)