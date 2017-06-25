#内嵌函数


def fun1():
    print('fun1() 正在被调用')
    def fun2():
        print('fun2() 正在被调用')
    fun2()  #返回执行结果

#闭包
def fx(x):
    x += 1
    def fy(y):
        return x*y
    return fy  #返回一个函数 等待被调用

fx(1)(2)


#递归函数  n! 3! = 3*2*1
'''
def factorial(n):
    temp = 0
    for i in range(1,n+1):
        temp = temp * i
    return temp
'''
#n! = n * (n-1).....
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)  #return 2 * factorial(1)

#回调函数
'''
from tkinter import *
root = Tk()
root.geometry('400x400+300+100')

def clik():
    print('哈哈哈')

Button(root,text='push',command=clik,bg='red').pack(fill=X,expand=1)
root.mainloop()
'''
