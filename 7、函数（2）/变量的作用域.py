#常见的内置函数

import keyword
##print(keyword.kwlist)
##dir(__builtins__)

la = ['a','z','c']
li = [2,8,5]

max(li)
len(li)
sorted(li)
reversed(li)
list(reversed(li))
tuple(reversed(li))
##dict()
set(reversed(li))


#####进制转换函数
bin(8) #转换二进制
oct(8)
'''
    bin()  转换为二进制
    oct()  转换为八进制
    hex() 转换为十六进制
    ord() 将字符转换成对应的ASCII码值
    chr() 将ASCII码值转换成对应的字符
'''

#lambda匿名函数
def fun1(x):
    x = x + 1
    return x

def fun2(x):
    return x + 1  #不能赋值 不能有等号

g = lambda x:x+1  #没有函数名字 ambda简化了函数定义的书写形式。


li = [(1,2),(3,4)]
k = lambda x:x[0][1]

# 3、函数内变量的作用域

def fun():
    x = 1
    return x
fun()
#a = 13   #全局
def fun_1():
    print(a)
    return a+1

#以上两种情况反映  内部管内部  全局不改变，改变需要用 global

def fun3():
    a = a+1
    print(a)
    return a  #函数内不能直接修改外部变量

def fun4(): #即便变量名相同  在函数内部和外部也会有区别,内部覆盖外部
    a = 0
    a = a+1
    print(a)
    return a

def fun5():
    global a  #global声明外部变量是可以在函数内部使用
    a = a+1
    return a


def fun6():
    b = 12
    def f7():
        nonlocal b  #nonlocal关键字用来在函数外层（非全局变量）
        b += 1
        return b
    print(f7())
