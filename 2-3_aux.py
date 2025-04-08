import RPi.GPIO as rp
import time

rp.setmode(rp.BCM)

leds = [ 2,  3,  4, 17, 27, 22, 10,  9]
ctrl = [21, 20, 26, 16, 19, 25, 23, 24]
rp.setup(leds, rp.OUT)
rp.setup(ctrl, rp.IN)

while True:
    for i in range(8):
        rp.output(leds[i], rp.input(ctrl[i]))
    time.sleep(0.1)