#!/usr/bin/python3
# This is a slightly modified version of this script:
# credits: http://yaab-arduino.blogspot.com/2016/08/display-two-digits-numbers-on-raspberry.html

from sense_hat import SenseHat

OFFSET_LEFT = 1
OFFSET_TOP = 1

NUMS =[0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,  # 0
       0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,  # 1
       1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

# Displays a single digit (0-9)
def show_digit(val, xd, yd, r, g, b, sense):
  offset = val * 15
  for p in range(offset, offset + 15):
    xt = p % 3
    yt = (p-offset) // 3
    sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])

# Displays a two-digits positive number (0-99)
def show_number(val, r, g, b, sense):
  abs_val = abs(val)
  tens = abs_val // 10
  units = abs_val % 10
  if (abs_val > 9): show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b, sense)
  show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b, sense)


if __name__ == '__main__':
    # just a tiny tesing setup :)

    import time
    from accelerometer import auto_orient
    sense = SenseHat()

    while True:
        i = input("Number to display (0-99): ")
        try:
            i = int(i)
        except:
            print("Not a number, try again")
            i = 0

        if i > 99 or i < 0:
            print("out of range!")
            i = 0
        sense.clear()
        show_number(i, 100, 0, 100, sense)
        auto_orient(sense)
        time.sleep(2)
        i += 1
