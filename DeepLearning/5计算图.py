#计算图

#计算图优点：可以通过正向传播和反向传播高效地计算各个变量的导数值。

#链式法则

#复合函数：如果某个函数由复合函数表示，则该复合函数的导数可以用构成复合函数的各个函数的导数的乘积表示。

#加法节点的反向传播：加法节点的反向传播只是将输入信号原封不动输出到下一个节点

#乘法节点的反向传播：将上游的值乘（导数）以正向传播时的输入信号的“翻转值”


class MulLayer:
    def __init__(self):
        self.x=None
        self.y=None

    def forward(self,x,y):
        self.x=x
        self.y=y
        out =x*y
        return out

# 根据乘法反向传播，
    def backward(self,dout):
        dx=dout*self.y
        dy=dout*self.x

        return dx,dy


apple_price=100
apple_num=2
tax=1.1

# layer
mul_apple_layer=MulLayer()
mul_tax_layer=MulLayer()

# forward
layer1=mul_apple_layer.forward(apple_num,apple_price)
layer2=mul_tax_layer.forward(layer1,tax)

print("forward:"+str(layer2))

#backward

d_price=1
d_apple_all_price,d_tax=mul_tax_layer.backward(d_price)
d_apple_sigle_price,d_apple_num=mul_apple_layer.backward(d_apple_all_price)

print(d_apple_sigle_price, d_apple_num, d_tax)
