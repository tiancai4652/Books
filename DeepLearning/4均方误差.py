import numpy as np

#均方误差会计算神经网络的输出和正确解监督数据的各个元素之差的平方，再求总和。

# 经过训练后，出现0-9的期望
y=[0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]

# 训练后的期望与实际期望的差值进行一定运算，其值越小越准确
def mean_squared_error(y,t):
    return 0.5*np.sum((y-t)**2)

# 测试数据，测试数据结果为2,即实际期望
t=[0,0,1,0,0,0,0,0,0,0]

print(mean_squared_error(np.array(y),np.array(t)))

# 测试数据，测试数据结果为7,即实际期望
t=[0,0,0,0,0,0,1,0,0,0]

print(mean_squared_error(np.array(y),np.array(t)))   