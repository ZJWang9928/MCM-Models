"""
 ____            _            _   _           
|  _ \  ___ _ __(_)_   ____ _| |_(_)_   _____ 
| | | |/ _ \ '__| \ \ / / _` | __| \ \ / / _ \
| |_| |  __/ |  | |\ V / (_| | |_| |\ V /  __/
|____/ \___|_|  |_| \_/ \__,_|\__|_| \_/ \___|
                                              
@author: Jonathan Wang
@coding: utf-8
@environment: Manjaro 18.1.5 Juhraya
@date: 19th Jan., 2020

"""

import scipy.misc as misc

# misc must be imported explicitly

def f(x):
    return 3*x**2 + 7*x + 8

if __name__ == '__main__':
    print(misc.derivative(f, 2))
