#!/usr/bin/python3
from sense_hat import SenseHat

def auto_orient(sense):
    # auto orients the led-screen based on the accelerometer in the SenseHat
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 0)
    y = round(y, 0)
    z = round(z, 0)

    if x  == -1:
        sense.set_rotation(90)
    elif y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(270)


if __name__ == '__main__':
    sense = SenseHat()
    sense.show_letter("A")
    while True:
        auto_orient(sense)
