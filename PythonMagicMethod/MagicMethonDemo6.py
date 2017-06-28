#八皇后问题
#首先寻找冲突
#找到一种没有冲突的位置(没有皇后会被其他的皇后吃掉）
def conflict(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False

#基本情况
#周后一个皇后能够根据其他皇后的位置生成他自己能占据的位置
def queens(num,state):
    if len(state)==num-1:
        for pos in range(num):
            if not conflict(state,pos):
                yield pos


#需要递归的情况
#递归函数需要假定所有的来自低层的结果都是正确的
#假定将位置信息作为一个元组返回，需要修改基本情况也返回一个元组
#这样一来，程序会从前面的皇后得到包含位置的元组信息，并且为后面的皇后提供当前皇后的每种合法位置信息
def queens2(num=8,state=()):
        for pos in range(num):
            if not conflict(state,pos):
                if len(state)==num-1:
                    yield (pos,)
                else:
                    for result in queens2(num,state+(pos,)):
                        yield (pos,)+result

#打包输出
def prettyprint(solution):
    def line(pos,length=len(solution)):
        return '. '*(pos)+'X '+'. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

import random
prettyprint(random.choice(list(queens2(100))))