#第二题答案、
"""
要求
有两个列表 x = [1,2,3,'a','b','c']  y = ['a','b','c']
找出x列表中在y 中也有的元素，
然后更新x，把在y中出现的元素去掉

"""
x = [1,2,3,'a','b','c']
y = ['a','b','c']

x1 = set(x) #转化为集合处理
y1 = set(y) #转化为集合处理

x1 & y1  #两者求交集
#print(x1 & y1)

x1.difference_update(y1) #更新x1去掉y1出现的元素

x = list(x1)

#print(x)

#第三题
"""
字典dic1 = {'number':123,'address':'changsha'}
	给dic1 添加两个key
	访问dic1中的所有key,和对应的值

"""
dic1 = {'number':123,'address':'changsha'}
#方法1
dic1.update({'age':18})
dic1.update({'sex':'Man'})

#方法2
dic1.setdefault('s',2)
dic1.setdefault('s1',3)

#方法3
dic1['a']=1
dic1['m']='M'


#1
l1 = list(dic1.items())
print(l1)
#2
l2 = list(dic1.keys())
print(l2)


#第四题
li = [1,2,'a']
tu = ('a','c',2,4,5)
dic2 = {'a':12,'i':'love'}
dic2.update({'abc':li})
dic2.update({'bcd':tu})
