# Широтно-импульсная модуляция
# Cкрипт, формирующий на выходе RC-цепи задаваемое
# широтно-импульсной модуляцией значение аналогового напряжения.


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
#   16 - пин из блока leds

# Cоздать объект управления ШИМ на выбранном GPIO-пине
t = GPIO.PWM(16,1000)

# Бесконечный цикл, 
# запрашивающий у пользователя коэффициент заполнения 
# и задающий введённый коэффициент объекту управления ШИМ
try:
    dc = 0
    voltage = 0
   # Запустить ШИМ с коэффициентом заполнения (duty cycle) 0
    print ("duty cycle")

    while True:
        dc = int(input())
        t.start(dc)
        voltage = 3.3/100 * dc
        print(voltage)

# Очистить настройки GPIO
finally:
    t.stop()
    GPIO.cleanup()