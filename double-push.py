import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)

leds = [16,12, 25, 17, 27, 23, 22, 24]

GP.setup(leds, GP.OUT)

GP.output(leds, 0)
butup = 9
butdown = 10
GP.setup(butup, GP.IN)
GP.setup(butdown, GP.IN)
num = 0
def dec2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GP.input(butup):
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GP.input(butdown)and num > 0:
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if num > 255:
        num = 0
    if GP.input(butup) and GP.input(butdown):
        num = 255
        time.sleep(sleep_time)
    GP.output(leds, dec2bin(num))
