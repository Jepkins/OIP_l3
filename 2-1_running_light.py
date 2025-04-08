import RPi.GPIO as rp
import time

rp.setmode(rp.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
rp.setup(leds, rp.OUT)

def trail():
    for i in leds:
        rp.output(i, rp.HIGH)
        time.sleep(0.2)
        rp.output(i, rp.LOW)

trail()
trail()
trail()

rp.cleanup()