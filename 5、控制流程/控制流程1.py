a = 1
b = 2
a == b
a != b
a > b
a < b

li = [1,2]
1 in li
2 not in li

id(a)
id(b)
a is b
a is not b

1 == 1 and 2 == 2 #与  两者相同为true
1 == 1 and 2 == 3

1 == 1 or 2 == 3  #或  一真为真
1 == 1 or 2 == 2

not 2 == 3   #非  


####控制流程
#条件语句
'''
a = 1
b = 2
if a > b: #if 后面True 才执行
    print('OK',a,b)
elif a < b:
    print('a<b',a,b)
else:
    #pass  #站位  什么也不做
    print('Error',a,b)
'''
#学号 判断
'''
a = 201706062
M = (a//1000)%10

if M == 5:
    print('你是11班')
elif M == 6:
    print('你是12班')
else:
    print('自己去算')
'''
#获取输入判断
'''
a = input('请输入您的学号：')#获取文本输入 class = str
#print(a)
#print(type(a))
a = int(a)
M = (a//1000)%10

if M == 5:
    print('你是11班')
elif M == 6:
    print('你是12班')
else:
    print('自己去算')
'''
'''
a = input('请输入您的学号：')
if len(a) == 9 and a.isdigit():  #嵌套最好不要超过三层
    a = int(a)
    M = (a//1000)%10  #ctrl + ]全部缩进

    if M == 5:
        print('你是11班')
    elif M == 6:
        print('你是12班')
    else:
        print('自己去算')
else:
    print('长度或者类型错误，请重新输入')
'''

#while
#死循环 False  None  {} [] 
'''
while(1):
    print('True')
'''
'''
a = 0
while a < 5: #终止条件
    print(a)
    a += 1   #自增    称好习惯  写循环尽量先把终止条件写好
'''

'''
while True:
    a = input('请输入您的学号:')
    if a == '0':
        break  #终止
    if len(a) == 9 and a.isdigit():
        a = int(a)
        M = (a//1000)%10
        if M == 5:
            print('你是11班的')            
        elif M == 6:
            print('你是12班')            
        else:
            print('自己去算')
    else:
        print('您输入的选号长度或者类型错误，请重新输入：')
'''
'''
c = 0
while c < 3:
    a = input('请输入您的学号:')
    if a == '0':
        break  #终止
    if len(a) == 9 and a.isdigit():
        a = int(a)
        M = (a//1000)%10
        if M == 5:
            print('你是11班的')            
        elif M == 6:
            print('你是12班')            
        else:
            print('自己去算')
    else:
        print('您输入的选号长度或者类型错误'+'还有'+str(3-c)+'次机会'+'请检查！')
    c += 1
'''

#continue
'''
a = 0
while a < 5:
    print(a)
    if a == 3:
        print(3)
    else:
        a += 1
        #continue  #继续  跳出本次循环 继续运行  后面的代码不执行
        break   #终止当前整个循环  不管什么条件
    a += 1
'''
# range   #得到一定范围内的数值 
list(range(10))
list(range(3,10))
list(range(3,10,2))

'''
a = 0
while a <= 100:
    if a%2 == 0:
        print(a,end = ' ')
    a += 1
'''
'''
for i in range(101):  #for 可迭代  依次取值
    if i%2 == 0:
        print(i)
'''
'''
li = [1,2,3]
for i in li:
    print(i)
    i = 'a'
    print(i)
'''
'''
b = 'qwe'
for i in b:
    print(i)
'''

c = {1:'a',2:'b'}
for i,j in c.items():
    print(i,j)
