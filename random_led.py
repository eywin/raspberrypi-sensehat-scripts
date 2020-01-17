from sense_hat import SenseHat
from random import randint, shuffle
import time

sense = SenseHat()
sense.clear() 
max_l = 47
current_l = 0

last_x = randint(0, 7)
last_y = randint(0, 7)

path = []
color = 0, 0, 255


def new_path():
    path = []
    for y in range(8):
        row = []
        for x in range(8):
            row.append(0)
        path.append(row)    
    
    return path


def reset_display():
    global path, current_l, last_x, last_y
    time.sleep(1)
    if current_l > 3:
        sense.clear()
    
    path = new_path()
    current_l = 0
    last_x = randint(0, 7)
    last_y = randint(0, 7)


def get_color():
    global current_l, color

    if current_l != 0:
        return color
    
    r = randint(0, 200)
    g = randint(0, 200)
    b = randint(0, 200)
       
    return r, g, b


def next_pixel():
    global path, last_x, last_y, current_l
    
    # up, right, down, left
    dirs = [(last_x, last_y-1), (last_x+1, last_y), 
            (last_x, last_y+1), (last_x-1, last_y)]

    shuffle(dirs)
    
    for x, y in dirs:
        if x < 0 or x > 7 or y < 0 or y > 7:
            continue

        if path[y][x] == 0:
            # path[y][x] = 1
            return x, y
    
    reset_display()
    return last_x, last_y


def loop():
    global current_l, max_l, last_x, last_y, color
    x, y = next_pixel()
    last_x = x
    last_y = y

    r, g, b = get_color()
    color = r, g, b
    
    path[y][x] = 1

    sense.set_pixel(x, y, 200, 200, 200)
    time.sleep(25 / 1000.0)
    sense.set_pixel(x, y, r, g, b)
    
    current_l += 1
    time.sleep(100 / 1000.0)
       

if __name__ == '__main__':
    path = new_path()
    # path[last_y][last_x] = 1
    while True: 
        loop()

