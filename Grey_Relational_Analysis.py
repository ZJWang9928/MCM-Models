"""
  ____ ____      _      __  __      _   _               _ 
 / ___|  _ \    / \    |  \/  | ___| |_| |__   ___   __| |
| |  _| |_) |  / _ \   | |\/| |/ _ \ __| '_ \ / _ \ / _` |
| |_| |  _ <  / ___ \  | |  | |  __/ |_| | | | (_) | (_| |
 \____|_| \_\/_/   \_\ |_|  |_|\___|\__|_| |_|\___/ \__,_|
                                                          

@author: Jonathan Wang
@coding: utf-8   
@environment: Manjaro 18.1.5 Juhraya + Python3.8.1 + pandas0.25.3
@date: 14th Jan., 2020

"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

red_wine = pd.read_csv('./src/datasets/wine/winequality-red.csv', sep=';')
print(red_wine.head)

def GRA_ONE(gray, m=0):
    gray = ((gray - gray.min()) / (gray.max() - gray.min()))
    
    std = gray.iloc[:, m]
    ce = gray.iloc[:, 0:]
    n, m = ce.shape[0], ce.shape[1]

    a = np.zeros([m, n])
    for i in range(m):
        for j in range(n):
            a[i, j] = np.abs(ce.iloc[j, i] - std[j])

    c, d = np.amax(a), np.amin(a)

    result = np.zeros([m, n])
    for i in range(m):
        for j in range(n):
            result[i, j] = (d + 0.5 * c) / (a[i, j] + 0.5 * c)

    return pd.DataFrame([np.mean(result[i, :]) for i in range(m)])


def GRA(DataFrame):
    list_cols = [
                str(s) for s in range(len(DataFrame.columns)) if s not in [None]
            ]
    print(list_cols)
    input()
    df_local = pd.DataFrame(columns=list_cols)
    for i in range(len(DataFrame.columns)):
        df_local.iloc[:, i] = GRA_ONE(DataFrame, m=i)[0]
    return df_local

def ShowGRAHeatMap(DataFrame):
    colormap = plt.cm.RdBu
    f, ax = plt.subplots(figsize=(14, 10.5))
    ax.set_title('GRA HeatMap')
    sns.heatmap(DataFrame.astype(float),
                cmap=colormap,
                ax=ax,
                annot=True,
                yticklabels=14,
                xticklabels=10)
    plt.show()


if __name__ == '__main__':
    data_wine_gra = GRA(red_wine)
    print(data_wine_gra)
    ShowGRAHeatMap(data_wine_gra)
