#创建一个构造方法
class fooBar:
    def __init__(self,value=42):
        self.somevar=value

f=fooBar()
print(f.somevar)
f=fooBar(1)
print(f.somevar)

#Python中有析构方法__del__，这个方法是在对象就要被垃圾回收之前调用，但是调用的时间是不可预测的，应该尽量避免使用

#重写超类方法
class A:
    def hello(self):
        print("Hello,I'm A")
class B(A):
    def hello(self):
        print("Hello,I'm B")
a=A()
b=B()
a.hello()
b.hello()

#调用未绑定的超类构造方法
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("eat")
            self.hungry=False
        else:
            print("no")

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound="lalal"
    def sing(self):
        print(self.sound)
sb=SongBird()
sb.sing()
sb.eat()
sb.eat()