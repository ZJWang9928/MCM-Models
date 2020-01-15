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

n = 100000
r = 1.0
a, b = 0.0, 0.0

y_max, y_min, x_max, x_min = b + r, b - r, a + r, a - r

x = np.random.uniform(x_min, x_max, n)
y = np.random.uniform(y_min, y_max, n)

distance = np.sqrt((x - a)**2 + (y - b)**2)
cnt = np.sum(np.where(distance <= r, 1, 0))

pi = 4 * cnt / n
print("Pi = ", pi)

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1)
plt.scatter(x, y, marker='.', s=10, alpha=0.5)
circle = Circle(xy=(a, b), radius=r, alpha=0.5, color='green')
ax.add_patch(circle)
ax.grid(color='k', linestyle='--', alpha=0.2, linewidth=2)

plt.show()
