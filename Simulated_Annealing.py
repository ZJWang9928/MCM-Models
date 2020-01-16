"""
 ____    _      __  __      _   _               _ 
/ ___|  / \    |  \/  | ___| |_| |__   ___   __| |
\___ \ / _ \   | |\/| |/ _ \ __| '_ \ / _ \ / _` |
 ___) / ___ \  | |  | |  __/ |_| | | | (_) | (_| |
|____/_/   \_\ |_|  |_|\___|\__|_| |_|\___/ \__,_|
                                                  
@author: Jonathan Wang
@coding: utf-8
@environment: Manjaro 18.1.5 Juhraya
@date: 16th, Jan., 2020

"""

import numpy as np
import matplotlib.pyplot as plt
import math

#  BOUND = [-100, 100]
BOUND = [0, 100]

def func(x):
    return x**3 - 60*x**2 - 4*x + 6

def SA():
    T_INITIAL = 10000
    T = T_INITIAL
    T_min = 10
    k = 50
    epsilon = 0.055
    y = 0
    t = 0
    x = np.random.uniform(BOUND[0], BOUND[1])

    while T > T_min:
        for i in range(k):
            y = func(x)
            x_neighbour = x + np.random.uniform(-epsilon, epsilon) * T
            if BOUND[0] <= x_neighbour and x_neighbour <= BOUND[1]:
                y_neighbour = func(x_neighbour)
                if y_neighbour < y:
                    x = x_neighbour
                else:
                    p = math.exp(-(y_neighbour - y) / T)
                    r = np.random.uniform(0, 1)
                    if r < p:
                        x = x_neighbour
        t += 1
        print('Cur Time: ', t)
        T = T_INITIAL / (1 + t)

    return x, func(x)
    

if __name__ == '__main__':
    x = np.linspace(BOUND[0], BOUND[1], num=2000)
    y = func(x)
    x_o, y_o = SA()
    print('Lowest Point: (%d, %d)' % (x_o, y_o))

    plt.figure()
    plt.plot(x, y)
    plt.plot(x_o, y_o, 'ro')
    plt.show()
