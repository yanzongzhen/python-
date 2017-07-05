#装饰器
# 复习 闭包
def fx(x):
    x += 1
    def fy(y):
        return x*y
    return fy


def f1(func):
    #print('f1 running')
    def f2(y):
        print('f2 runing')
        return func(y) + 1
    return f2

def gun(m):
    print('gun running')
    print (m * m)

# f1(gun)
#fg = f1(gun)
#fg(1)

@f1
def deco(m):
    print('this is deco')
    return m*m  #通过装饰圈  实现给deco返回值加1的功能

'''
装饰器的作用就是为已经存在的对象添加额外的功能
'''

#  测试功能运行时间

import time
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args)
        print('end time: %s'%(time.strftime('%x',time.localtime())) )
        print('run time: %s'%(time.time() - t0))
        return back
    return new_fun


@run_time #调用装饰器
def test():
    for i in range(1,10):
        for k in range(1,10):
            if i <= k:
                print('%dx%d=%2d'%(i,k,i*k),end=' ')
    print()


class Test_class:
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print('class')
        return self.func

@Test_class
def fun_test():
    print('这是测试')

#fun_test()()

#4 类装饰器
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        areas = self.length * self.width
        return area

    @property  #直接访问类属性
    def fun(self):
        return self.width,self.length
    
    @staticmethod  #直接返回  不需要self
    def fun1():
        print('staticmethod')

    @classmethod   #cls == Rectangle
    def show(cls):
        print(cls)
        print('show fun')


e = Rectangle(3,4)
f = Rectangle(5,6)


#框架时候用 一般不会用
    

