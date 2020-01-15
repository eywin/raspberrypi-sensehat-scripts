#!/usr/bin/python3
import math
import time
from sense_hat import SenseHat


def display_secs(sense, secs, color, row=7): 
    # row: 0 is the top, 7 is the bottom
    frac, whole = math.modf((secs / 60) * 8)
    pixels = int(whole)

    dim_c = [0, 0, 0]
    for i in range(3):
        dim_c[i] = int(color[i] * frac)

    for p in range(8):
        if p == pixels:
            sense.set_pixel(p, row, dim_c)
        elif p < pixels:
            sense.set_pixel(p, row, color)
        else:
            sense.set_pixel(p, row, [0, 0, 0])


if __name__ == '__main__':
    sense = SenseHat()
    c = [100, 255, 0]
    sense.clear()
    i = 0
    reverse = False 
    while True:
        display_secs(i, c)
        time.sleep(0.1)
        if i == 60:
            reverse = True
        elif i == 0:
            reverse = False
        
        if reverse:
            i -= 1
        else:
            i += 1
