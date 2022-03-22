# Задача №3. Отобразить состояние входа светодиодом

import RPi.GPIO as GPIO
#import time

GPIO.setmode(GPIO.BCM)

# Настроить один выбранный GPIO-пин как вход
GPIO.setup(23, GPIO.IN)

# Настроить другой выбранный GPIO-пин, как выход
GPIO.setup(15, GPIO.OUT)

#Считать значение со входа
#Подать считанное значение на выход

while True:
    GPIO.output(15, GPIO.input(23))

 

 


