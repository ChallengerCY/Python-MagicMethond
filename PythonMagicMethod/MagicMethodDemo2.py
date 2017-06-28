#使用super函数
#当前的类和对象可以作为super函数的参数使用，调用返回的对象的任何方法都是
#super函数会自动寻找他所需要的特性，直到返回一个AttributeError异常
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
        super(SongBird,self).__init__()
        self.sound="lalal"
    def sing(self):
        print(self.sound)

sb=SongBird()
sb.sing()
sb.eat()
sb.eat()

#子类化列表，字典和字符串
#带有访问计数的列表
class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter=0
    def __getitem__(self, item):
        self.counter+=1
        return super(CounterList,self).__getitem__(item)
c1=CounterList(range(10))
print(c1)
c1.reverse()
print(c1)
del c1[3:5]
print(c1)
print(c1.counter)
print(c1[4]+c1[2])
print(c1.counter)

