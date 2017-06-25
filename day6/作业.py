'''
函数作业1

1.把老师上课的例子敲一遍

2.判断1 - 100 内能够被 3 和 5 整除的数，用while和for循环来做

3.定义包含各种参数形式的函数，并调用

4.定义一个函数，能够输入字典和元组，返回一个字典，字典的值，用元组的值替换
'''

#for
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
#while
a = 1
while a <= 100:
    if a % 3 == 0 and a % 5 == 0:
        print(a)
    a += 1


def fun_all(x,y=1,*arg,**kwarg):
    print('this is x:',x)
    print('this is y:',y)
    print('this is args:',arg)
    print('this is kwargs:',kwarg)
    
#传必备参数值 同时默认参数传回
fun_all(1)
'''
输出值
this is x: 1
this is y: 1
this is args: ()
this is kwargs: {}
'''
#传默认参数（必备参数必须），修改默认参数值 结果
'''
输出结果
this is x: 1
this is y: 2
this is args: ()
this is kwargs: {}
'''
#前两者存在 定义一个元组  一个字典
tu = (1,2,3,4,5)
di = {'a':1,'b':2}
fun_all(1,2,tu,di)
'''
直接传字典无法将字典存入
this is x: 1
this is y: 2
this is args: ((1, 2, 3, 4, 5), {'a': 1, 'b': 2})
this is kwargs: {}

'''
fun_all(1,2,tu,di,a=1,b=2,c=3)
'''
这样就可以传入字典
this is x: 1
this is y: 2
this is args: ((1, 2, 3, 4, 5), {'a': 1, 'b': 2})
this is kwargs: {'a': 1, 'b': 2, 'c': 3}
'''
fun_all(1,2,*tu,**di)
'''
加符号指向就可以直接加入字典
this is x: 1
this is y: 2
this is args: (1, 2, 3, 4, 5)
this is kwargs: {'a': 1, 'b': 2}
'''
