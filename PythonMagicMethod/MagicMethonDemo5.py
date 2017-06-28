#从迭代器得到序列
#除了再迭代器和可迭代对象向上进行迭代，还可以把他们转换成序列
class TestIterator:
    value=0
    def __next__(self):
        self.value+=1
        if self.value>10:raise StopIteration
        return self.value
    def __iter__(self):
        return self
t1=TestIterator()
print(list(t1))

#创建生成器
nested=[[1,2],[3,4],[5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
#包含yield语句的函数成为生成器，他不想return一样返回值，而是每次产生多个值，每产生一个值，函数就会冻结，(函数会暂时冻结，等待唤醒，重新唤醒后就会从停止的地方开始执行)

for num in flatten(nested):
    print(num)

print(list(flatten(nested)))

#递归生成器
def flatten2(nested):
    try:
        try:nested+''
        except TypeError:pass
        else:raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
print(list(flatten2([[[1],2],3,4,[5,[6,7]],8])))
print(list(flatten2(['foo',['bar',['baz']]])))

#生成器方法
#生成器有三个方法
#close,throw,send
def repeater(value):
    while True:
        new =(yield value)
        if new is not None:value=new

r=repeater(42)
print(next(r))
print(r.send("hello,world"))
