"""
 ____  ____   ___    __  __      _   _               _ 
|  _ \/ ___| / _ \  |  \/  | ___| |_| |__   ___   __| |
| |_) \___ \| | | | | |\/| |/ _ \ __| '_ \ / _ \ / _` |
|  __/ ___) | |_| | | |  | |  __/ |_| | | | (_) | (_| |
|_|   |____/ \___/  |_|  |_|\___|\__|_| |_|\___/ \__,_|
                                                       
@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1
@date: 14th Jan., 2020

"""

import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
import matplotlib.pyplot as plt

# Set-up optimizer
options = {'c1':0.5, 'c2':0.3, 'w':0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=50, dimensions=2, options=options)
best_cost, best_pos = optimizer.optimize(fx.sphere, iters=100) # f(x) = x**2
print("Best Cost: ", best_cost)
print("Best Position: ", best_pos)

# Plot the cost
plot_cost_history(optimizer.cost_history)
plt.show()
