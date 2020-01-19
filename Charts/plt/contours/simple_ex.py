import numpy as np
import matplotlib.pyplot as plt

def f(x, y, w=5, sigma=2):
    return np.sin(w*x)**2 * np.sin(w*y)**2 * np.exp((x+y)/sigma)

n = 256
x = np.linspace(0, 3, n)
y = np.linspace(0, 3, n)
X, Y = np.meshgrid(x, y)

C = plt.contour(X, Y, f(X, Y),  8, colors='black')

plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='gray_r')
plt.clabel(C, inline=True, fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()
