import numpy as np

#交叉熵误差的值是由正确解标签所对应的输出结果决定的。

#作为保护性对策，添加一个微小值可以防止负无限大的发生

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))

# 经过训练后，出现0-9的期望
y=[0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]

# 测试数据，测试数据结果为2,即实际期望
t=[0,0,1,0,0,0,0,0,0,0]

print(cross_entropy_error(np.array(y),np.array(t)))

# 测试数据，测试数据结果为7,即实际期望
t=[0,0,0,0,0,0,1,0,0,0]


print(cross_entropy_error(np.array(y),np.array(t)))