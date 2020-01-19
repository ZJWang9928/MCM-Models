import numpy as np
import matplotlib.pyplot as plt

step = 0.01
x = np.arange(-10, 10, step)
y = np.arange(-10, 10, step)
# 也可以用x = np.linspace(-10,10,100)表示从-10到10，分100份

# 将原始数据变成网格数据形式
X,Y = np.meshgrid(x, y)
Z = X**2+Y**2

cset = plt.contourf(X,Y,Z,6,cmap=plt.cm.hot)
# or cmap='hot'
# 取反加'_r'

# 画出8条线，并将颜色设置为黑色
contour = plt.contour(X,Y,Z,8,colors='k')

# 只画高为0.00221，和0.00223的线
# contour = plt.contour(X,Y,Z,[0.00221,0.00223],colors='k')

# 等高线上标明z（即高度）的值，字体大小是10，颜色分别是黑色和红色
plt.clabel(contour,fontsize=10,colors='k')

# 去掉坐标轴刻度
plt.xticks(())
plt.yticks(())

# 设置颜色条，（显示在图片右边）
plt.colorbar(cset)

plt.show()
