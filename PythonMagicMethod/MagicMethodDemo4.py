#__getattr__、__setattr__
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self, key, value):
        if key=='size':
            self.width,self.height=value
        else:
            self.__dict__[key]=value
    def __getattr__(self, item):
        if item=='size':
            return self.width,self.height
        else:
            raise AttributeError

d=Rectangle()
d.height=10
d.width=10
print(d.__getattr__(item='size'))
d.__setattr__(key='size',value=(100,200))
print(d.height)

#迭代时候最好不要用列表，如果有很多值，列表会占用太多的内存
#使用迭代器更通用，更简单，更优雅。
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
#一个实现了__iter__方法的对象是可以迭代的，一个实现了__next__方法的对象则是迭代器
fibs=Fibs()
for f in fibs:
    if f>1000:
        print(f)
        break
#内建函数iter可以从可迭代的对象中获得迭代器
it=iter([1,2,3])
print(next(it))
print(next(it))
print(next(it))
