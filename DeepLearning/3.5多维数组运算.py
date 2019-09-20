
import numpy as np


#一维数组
n1=np.array([1,2,3,4])
print(n1)
print("空间维数:"+str(np.ndim(n1)))


#二维数组
n2=np.array([[1,2],[2,3],[4,5]])
print(n2)
print(np.ndim(n2))


#矩阵相乘

n3 = np.array([[1, 2, 3], [4, 5, 6]])
n4 = np.array([[1, 2], [3, 4], [5, 6]])
n5=np.dot(n3,n4)
print(n5)


#实现神经网络

X=np.array([1,2])
W=np.array([[1,2,5],[2,4,6]])
Y=np.dot(X,W)
print('here we are')
print(Y)