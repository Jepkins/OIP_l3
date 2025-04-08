import RPi.GPIO as rp
import time

num_int = int(input("num = "))
num_bin = [0,0,0,0,0,0,0,0]
for i in range(8):
    num_bin[7 - i] = num_int % 2
    num_int //= 2

print(num_bin)
rp.setmode(rp.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]


rp.setup(dac, rp.OUT)
rp.output(dac, num_bin)

time.sleep(10)

rp.cleanup()