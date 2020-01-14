 #  _     _                         __  __           _      _ 
#  | |   (_)_ __   ___  __ _ _ __  |  \/  | ___   __| | ___| |
#  | |   | | '_ \ / _ \/ _` | '__| | |\/| |/ _ \ / _` |/ _ \ |
#  | |___| | | | |  __/ (_| | |    | |  | | (_) | (_| |  __/ |
#  |_____|_|_| |_|\___|\__,_|_|    |_|  |_|\___/ \__,_|\___|_|

import numpy as np
import matplotlib.pyplot as plt

mass = [50*i for i in range(1, 12)]
length = [1.000,1.875,2.750,3.250,4.375,4.875,5.675,6.500,7.250,8.000,8.750]
F = np.polyfit(mass, length, 1)
print(F)
P = np.poly1d(F)
print(P)

y = F[0] * np.array(mass) + F[1]

plt.figure()
plt.scatter(mass, length)
plt.plot(mass, y, color='r')
plt.show()
