#property函数
#将访问器函数被用作参数
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
    size=property(getSize,setSize)

r=Rectangle()
r.width=10
r.height=5
print(r.size)
r.size=150,100
print(r.width)

#静态成员方法和类成员方法
class MyClass:
    def smeth():
        print("This is a static method")
    smeth=staticmethod(smeth)

    def cmeth(cls):
        print("This is a class methon of'",cls)
        cmeth=classmethod(cls.cmeth)
#装饰器
class MyClass1:
    @staticmethod
    def smeth():
        print("This is a static method")

    @classmethod
    def cmeth(cls):
        print("This is a class method",cls)

cla=MyClass1()
cla.smeth()
cla.cmeth()