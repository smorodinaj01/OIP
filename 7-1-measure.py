import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def bin2dec(list):
    weight = 128
    val = 0
    for i in range(0, 8):
        val += weight * list[i]
        weight /= 2
    
def adc_sar():
    list = [0] * 8
    for i in range(0, 8):
        list[i] = 1
        GPIO.output(dac, list)
        time.sleep(0.001)

        if(GPIO.input(comp) == 0):
            list[i] = 0

    return bin2dec(list)

data = []

try:
    start_time = time.time()
    print("Зарядка началась")
    GPIO.output(troyka, 1)

    val = 0
    while(val <= 255 * 0.97):
        val = adc_sar()
        data.append(val)
        print("Voltage: {:.2f} V".format(tmp * 3.3 / 256))
        GPIO.output(leds, dec2bin(val))
    
    charge_time = time.time() - start_time
    
    GPIO.output(troyka, 0)

    val = 255
    while (val >= 255 * 0.02):
        val = adc_sar()
        data.append(val)
        print("Voltage: {:.2f} V".format(val * 3.3 / 256))
        GPIO.output(leds, dec2bin(val))
    
    finish_time = time.time() - start_time
        
finally:
    print("Конец")
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.plot(data)
plt.show()

data_str = [str(item) for item in data]

with open("7-1_data.txt", "w") as outfile:
    outfile.write("\n".join(data_str))

with open("7-1_settings.txt", "w") as outfile:
    outfile.write("discret: {} s\nquant: {:.5f} V".format(finish_time / len(data), 3.3 / 256))