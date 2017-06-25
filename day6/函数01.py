#while 和 for
#
#
''' break 和 continue 的区别细分
    break 会终止本层循环
    continue 会跳过本层本次循环
    break和continue都只作用与本次循环，不会影响外循环
'''
'''
a = 0
while a < 5:
    print('aaa',a)
    a += 1
    b = 0
    while b < 3:
        b += 1
        if b == 2:
            #continue   作用于本次循环会跳过本层本次循环
            break        #终止本层循环  本次  
        print('b',b)
    print('cccccccc')
'''
'''
for i in range(5):
    print('iiii',i)
    for k in range(5):
        if k == 2:
            #continue
            break
        print('kk',k)
'''
###else   while   for
'''
a = 0
while a < 5:
    if a == 3:
        print(a)
    a += 1
else:
    print('OK')
'''
'''
a = 0
while a < 5:
    if a == 3:
        print(a)
        break
    a += 1
else:
    print('OK')
'''
'''
import random
a = random.randint(1,10)
#print(a)
c = 0
while c < 3:
    b = input('请输入：')
    b = int(b)
    if b > a:
        print('大了')
    elif b < a:
        print('小了')
    else:
        print('对了')
        break
    c += 1
else:
    print('次数用完了')
'''

for i in range(5):
    if i == 3:
        print(i)
        #break   #终止结束 不继续进行
        continue #跳出   继续进行
else:
    print('OK')

###引入
''' 一个数字组成的列表  每次去其中两个做判断大小，最后找到列表最大的'''
'''
li = [2,5,6,9]
li[0]
if li[0] >= li[1]:
    temp = li[0]
else:
    temp = li[1]

if temp >= li[2]:
    temp = temp
else:
    temp = li[2]

if temp >= li[3]:
    temp = temp
else:
    temp = li[3]

print(temp)
'''
'''
li = [2,5,6,9]
for i in range(len(li)-1):  #获取列表长度
    if li[i] >= li[i+1]:
        temp = li[i]
    else:
        temp = li[i+1]
print(temp)
'''
'''
li = [3,2,5,7,8]
def max_list(la):
    for i in range(len(la)-1):  #获取列表长度
        if li[i] >= la[i+1]:
            temp = la[i]
        else:
            temp = la[i+1]
    return temp
'''
######函数
'''
定义方法：
def function_name(params):
        block
        return expression(表达式)/value
'''

#####################
#      参数详解     #
#####################
#必备参数，没有默认值  可以改变传值顺序  可以使用参数名  参数没有默认值为必备参数
'''
def fun(x,y):
    print('xxx',x)
    print('y',y)
fun(1,2)
fun(x=1,y=2)
fun(y=2,x=1)#最好不要这么做
'''
#以下的x没有默认值为必备参数必须传入给函数  有值的为默认参数  可具体参数传值
'''
def fun_test(x,y=2,z=3):
    print('function')
    print('paramsx is:',x)
    print('paramsy is:',y)
    print('paramsz is:',z)
    print(x**2)
    print(x*y)
    print(x*y*z)

fun_test(1)
fun_test(1,4)
fun_test(1,4,2)
fun_test(x=1,z=5)

#不要用
def test(a = None,):
    print('test')
'''
#########################################################
#关键字参数：传参时出入参数名和参数值可以改变传参的顺序 #
#########################################################


#不定长参数  元组args字典 **kwargs

'''
#定义时定义一个元组
def func_arg(a,z=1,*arg):
    print(a)
    print(z)
    print(arg)
    
func_arg(1,2,3)
func_arg(1,2,3,4,5,6,)
'''
'''
def func_ac(a,z=3,b=2):
    print(a)
    print(z)
    print(b)
    
tu = (1,2,3)
func_ac(*tu)
'''
'''
def func_kw(**kwargs):
    print(kwargs)
'''
'''
def fun_kw(*arg,**kwargs):
    print(arg)
    print(kwargs)

di = {'a':1,'b':2}
tu = (1,2,3)
fun_kw(*tu,**di)
fun_kw(tu,di,a=1,b=2)
'''
