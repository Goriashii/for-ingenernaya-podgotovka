import RPi.GPIO as GP
import time 

GP.setmode(GP.BCM)

leds = [24, 22, 23, 27, 17,25, 12, 16]

GP.setup(leds, GP.OUT)

GP.output(leds,0)
light_time = 0.1
while True:
    for led in leds:
        GP.output(led, 1)
        time.sleep(light_time)
        GP.output(led, 0)
    for led in reversed(leds):
        GP.output(led, 1)
        time.sleep(light_time)
        GP.output(led, 0)
