import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
clean_bin = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup (dac, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def prob_out(binary):
    s = 0
    for i in range(7, -1, -1):
        s += binary[i] * 2**(7 - i)
    return s * (3.3/256)


try:
    while (1):
        symbol = (input("Введите число для ЦАП: "))
                
        if symbol == "q":
            break
        
        try:    
            symbol = int(symbol)

            if symbol < 0:
                print ("Введено отрицательное число.")
                continue
            #    break
            if symbol > 255:
                print ("Число слишком велико.")
                continue
            #    break

            binary = dec2bin(symbol)

        except ValueError:
            print ("Ошибка ввода.")
            continue

        else:
        
            GPIO.output(dac, binary)
            print(binary)
            print ("Напряжение:", "{:.4}".format(prob_out(binary)))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()