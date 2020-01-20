"""
  ____                         ___   __   _     _  __      
 / ___| __ _ _ __ ___   ___   / _ \ / _| | |   (_)/ _| ___ 
| |  _ / _` | '_ ` _ \ / _ \ | | | | |_  | |   | | |_ / _ \
| |_| | (_| | | | | | |  __/ | |_| |  _| | |___| |  _|  __/
 \____|\__,_|_| |_| |_|\___|  \___/|_|   |_____|_|_|  \___|
                                                           
@author: Jonathan Wang
@coding: utf-8
@environment: Manjaro 18.1.5 Juhraya
@date: 20th Jan., 2020

"""

import numpy as np
import matplotlib.pyplot as plt

class GameOfLife(object):

    def __init__(self, cells_shape):
        """
        cells_shape: tuple, size of the canvas
        """

        # edges of the canvas are not calculated
        self.cells = np.zeros(cells_shape)

        real_width = cells_shape[0] - 2
        real_height = cells_shape[1] - 2

        self.cells[1: -1, 1: -1] = np.random.randint(2, size=(real_width, real_height))
        self.timer = 0
        self.mask = np.ones(9)
        self.mask[4] = 0

    def update_state(self):
        buf = np.zeros(self.cells.shape)
        cells = self.cells
        for i in range(1, cells.shape[0] - 1):
            for j in range(1, cells.shape[0] - 1):
                # count live neighbours
                neighbour = cells[i-1:i+2, j-1:j+2].reshape((-1,))
                neighbour_num = np.convolve(self.mask, neighbour, 'valid')[0]

                if neighbour_num == 3:
                    buf[i, j] = 1
                elif neighbour_num == 2:
                    buf[i, j] = cells[i, j]
                else:
                    buf[i, j] = 0
        self.cells = buf
        self.timer += 1

    def plot_state(self):
        plt.title('Iter :{}'.format(self.timer))
        plt.imshow(self.cells)
        plt.show()

    def update_and_plot(self, n_iter):
        plt.ion()
        for _ in range(n_iter):
            plt.title('Iter :{}'.format(self.timer))
            plt.imshow(self.cells)
            self.update_state()
            plt.pause(0.2)
        plt.ioff()

if __name__ == '__main__':
    game = GameOfLife(cells_shape=(40, 40))
    game.update_and_plot(200)
