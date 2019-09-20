class Layer:
    def __init__(self):
        self.x=None
        self.y=None
        self.out=None

    #赋值实际值
    def Go(self,x,y):
        self.x=x
        self.y=y
        self.out=x.value*y.value
      
    
    #赋值导数值
    def GoBack(self,dout):
        self.x.dvalue=dout*self.y.value
        self.y.dvalue=dout*self.x.value
        return self.x,self.y


    def OutPut(self):
        tmp=Objct()
        tmp.value=self.out
        return tmp


class Objct:
    def __init__(self):
        #实际值
        self.value=None
        #导数值
        self.dvalue=None



apple_price=Objct()
apple_num=Objct()
tax=Objct()
apple_price.value=100
apple_num.value=2
tax.value=1.1

Layer1=Layer()
Layer1.Go(apple_price,apple_num)

Layer1Object=Layer1.OutPut()

Layer2=Layer()
Layer2.Go(Layer1Object,tax)

Layer2Object=Layer2.OutPut()

Layer2Object.dvalue=1

Layer1Object,tax=Layer2.GoBack(Layer2Object.dvalue)

apple_price,apple_num=Layer1.GoBack(Layer1Object.dvalue)

def PrintObject(a):
    print(a.value,a.dvalue)

PrintObject(apple_price)
PrintObject(apple_num)
PrintObject(tax)
#PrintObject(Layer1Object)
#PrintObject(Layer2Object)