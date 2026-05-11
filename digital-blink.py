import RPi.GPIO as GPIO

U = 3.15

def voltage_to_number(voltage):
    if not (0.0 <= voltage <=U):
        print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {U:.2f} В)")
        return 0
    return int(voltage / U * 255)


def namber_to_dac(number):

    return [int(i) for i in bin(number)[2:].zfill(8)]

dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]
dac_bits = dac_bits[::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)

try:
    while True:
        try:
            voltage = float(input("введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            GPIO.output(dac_bits, namber_to_dac(number))
        except ValueError:
            print("вводи число")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()



    
                


