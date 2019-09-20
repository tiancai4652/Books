#神经网络的一个重要性质是它可以自动地从数据中学习到合适的权重参数

import numpy as np

def step_function(x):
    if x>0:
        return 1
    else:
        return 0

def step_function_array(x):
    y=x>0
    return y.astype(np.int)