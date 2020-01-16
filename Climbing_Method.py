"""
  ____ _ _           _     _               __  __      _   _               _ 
 / ___| (_)_ __ ___ | |__ (_)_ __   __ _  |  \/  | ___| |_| |__   ___   __| |
| |   | | | '_ ` _ \| '_ \| | '_ \ / _` | | |\/| |/ _ \ __| '_ \ / _ \ / _` |
| |___| | | | | | | | |_) | | | | | (_| | | |  | |  __/ |_| | | | (_) | (_| |
 \____|_|_|_| |_| |_|_.__/|_|_| |_|\__, | |_|  |_|\___|\__|_| |_|\___/ \__,_|
                                   |___/                                     

@author: Jonathan Wang
@coding: utf-8
@environment: Manjaro 18.1.5 Juhraya
@date: 16th Jan., 2020

"""

import math
import numpy as np
import matplotlib.pyplot as plt

STEP = 0.01
BOUND = [5, 8]
GENERATION = 1000

def func(x):
    return math.sin(x**2) + 2.0*math.cos(2.0*x)

def Climbing(x):
    while func(x + STEP) > func(x) and x + STEP <= BOUND[1] and x + STEP >= BOUND[0]:
        x += STEP
    while func(x - STEP) > func(x) and x - STEP <= BOUND[1] and x - STEP >= BOUND[0]:
        x -= STEP
    return x, func(x)

def Solve():
    highest = [0, -1e100]

    for i in range(GENERATION):
        x = np.random.rand() * (BOUND[1]-BOUND[0]) + BOUND[0]
        cur_value = Climbing(x)
        print('Current value = ', cur_value)

        if cur_value[1] > highest[1]:
            highest = cur_value

    return highest

if __name__ == '__main__':
    x, y = Solve()
    print('Highest Point: (%f, %f)' % (x, y))
