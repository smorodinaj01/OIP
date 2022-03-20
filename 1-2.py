# Задача №2. Поморгать светодиодом

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Настроить выбранный GPIO-пин, как выход
GPIO.setup(15, GPIO.OUT)

#Подать на выбранный GPIO-пин единицу
GPIO.output(15, 1)

# Подождать
time.sleep(2)

#Подать на выбранный GPIO-пин ноль
GPIO.output(15, 0)

#Подождать
time.sleep(2)

#########
GPIO.output(15, 1)

# Подождать
time.sleep(2)

#Подать на выбранный GPIO-пин ноль
GPIO.output(15, 0)

#Подождать
time.sleep(2)

##########

GPIO.output(15, 1)

# Подождать
time.sleep(2)

#Подать на выбранный GPIO-пин ноль
GPIO.output(15, 0)

#Подождать
time.sleep(3)





 