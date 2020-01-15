"""
 __  __             _          ____           _       
|  \/  | ___  _ __ | |_ ___   / ___|__ _ _ __| | ___  
| |\/| |/ _ \| '_ \| __/ _ \ | |   / _` | '__| |/ _ \ 
| |  | | (_) | | | | ||  __/ | |__| (_| | |  | | (_) |
|_|  |_|\___/|_| |_|\__\___|  \____\__,_|_|  |_|\___/ 
                                                      
@author: Jonathan Wang
@coding: utf-8
@environment: Manjaro 18.1.5 Juhraya
@date: 15th Jan., 2020

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# func: f(x) = x ** 2

n = 100000

y_max, y_min, x_max, x_min = 5.0, 0.0, 1.0, 0.0

x = np.random.uniform(x_min, x_max, n)
y = np.random.uniform(y_min, y_max, n)

def func(x):
    return 4 * x ** 3 + x ** 2

cnt = np.sum(np.where(y < func(x), 1, 0))

res = cnt / n
print("Res = ", res)

fig = plt.figure(figsize=(12, 12))
axes = fig.add_subplot(1, 1, 1)
axes.plot(x, y, 'o', markersize=1)
xi = np.linspace(0, 1, 100)
yi = func(xi)
plt.plot(xi, yi, '--r')
plt.fill_between(xi, yi, 0, color='green', alpha=0.5, label='area')
plt.grid()
plt.show()
