#第二题
'''
给一个不多于5位的真正数
要求：1、求他是几位数
      2、逆序打印出来个位数字
'''
'''
a = input('请输入数字：')
if len(a) <= 5:
    print('这是一个%s位数字'%(len(a)))
    b = list(a)
    b.reverse()
    print(b,end=' ')
'''

#第二题  9*9口诀表
'''
print('***************************乘法口诀表******************************')
for i in range(1,10):
    for k in range(1,10):
        if i <= k:
            print('%dx%d=%2d'%(i,k,i*k),end=' ')
    print()
print('****************************乘法口诀表*****************************')     
'''


#第四题  两个列表x和y，要求y中也有的元素就从x中移除
'''
x = [1,2,'a','b','c',4]
y = [2,4,'a',4,6]

x1 = set(x)
y1 = set(y)

x1.difference_update(y1) #去掉相同的
print(x1)
'''
x = [1,2,'a','b','c',4]
y = [2,4,'a',4,6]
for i in y:
    #print(y.index(i),i)
    for k in x:
        if i == k:
            x.remove(i)
print(x)        
