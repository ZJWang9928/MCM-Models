"""
    _    _   _ ____    __  __      _   _               _ 
   / \  | | | |  _ \  |  \/  | ___| |_| |__   ___   __| |
  / _ \ | |_| | |_) | | |\/| |/ _ \ __| '_ \ / _ \ / _` |
 / ___ \|  _  |  __/  | |  | |  __/ |_| | | | (_) | (_| |
/_/   \_\_| |_|_|     |_|  |_|\___|\__|_| |_|\___/ \__,_|

@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1 + numpy1.17.4
@date: 13th Jan., 2020

"""

import numpy as np

RI_lst = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51]

def get_vec(x):
    num_rows = x.shape[0]
    x_col_sum = x.sum(axis=0)
    x1 = x / x_col_sum
    x1_row_sum = x1.sum(axis=1)
    vec = x1_row_sum / num_rows
    AW = (vec * x).sum(axis=1)
    max_lambda = np.sum(AW / (num_rows * vec))
    
    CI = (max_lambda - num_rows) / (num_rows - 1)
    CR = CI / RI_lst[num_rows]

    if CR < 0.1:
        return vec
    else:
        print("CR = %.3d, consistency violated.")

def AHP(A, B):
    a = get_vec(A)
    for i in range(B.shape[0]):
        if i == 0:
            b = np.expand_dims(get_vec(B[i]), 0)
        else:
            b = np.concatenate((b, np.expand_dims(get_vec(B[i]), 0)), 0)
    res = (np.transpose(b) * a).sum(axis=1)
    print("Res: ", res)


if __name__ == '__main__':
    A = np.array([
        [1,1/2,4,3,3],
        [2,1,7,5,5],
        [1/4,1/7,1,1/2,1/3],
        [1/3,1/5,2,1,1],
        [1/3,1/5,3,1,1],
        ])
    B = np.array([
        [
            [1,2,5],
            [1/2,1,2],
            [1/5,1/2,1],
            ],
        [
            [1,1/3,1/8],
            [3,1,1/3],
            [8,3,1],
            ],
        [
            [1,1,3],
            [1,1,3],
            [1/3,1/3,1],
            ],
        [
            [1,3,4],
            [1/3,1,1],
            [1/4,1,1],
            ],
        [
            [1,1,1/4],
            [1,1,1/4],
            [4,4,1],
            ],
        ])
    AHP(A, B)
