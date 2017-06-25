#-*-coding:UTF-8-*-

#字符串  格式化 转义符
a = 'aaa'
'%s'%(a) #不输出引号
'%r'%(a) #输出引号

tu = (1,2,3,4,5)
t1 = 1,2,3,4,6
t2 = 'a','b','c','d'

#元组  不可变  方法count index

tu.count(1)
tu.index(2)

#元组列表嵌套
li = [1,2,3,4,5,6,3,2,1]
tup = ('a','b','c','d','e')

ls = ['a',li]  #列表内嵌列表  li[][]  
li = ['b',tup] #列表内嵌元组
tu = ['c',li]  #元组内嵌列表
tu = ['c',tup] #元组内嵌元组   tu[][]
'abcd{}efg'.format(li)
#嵌套后属性不变

#深复制和浅复制
#浅复制   新建引用  未变对象
cols = ls.copy()
li[0] = 'a'
id(ls),id(cols)
id(li),id(ls[1]),id(cols[1])

#深复制  对于列表新建一个对象
import copy
aa = copy.deepcopy(ls)
id(ls),id(aa)


#浅复制  copy  切片 赋值

#保留改变的数据

#集合
se = {1,2,3,3,3,'a','b','c',tup}
"""
特点：
无序
不重复

"""
sa =  set(['e','f','g'])
s2 = set(tu)

#交集 并集 差集
se & s2  #求同  
se - s2  #存异  se.differnce
sa  | se #全部放入不能重复

se.add('w')  #添加命令
#se.clear()
se.difference(s2)
se.difference_update(s2)

#se.discard('a')
se.intersection(s2) #交集
se.isdisjoint(s2)  #无交集返回True  有交集返回False

se.issubset(s2)  #判断se是否为s2子集
s2.issuperset(se)  #判断是s2为se父集
se.pop()
se.remove(2)
se.symmetric_difference(s2)  #差集
se.union(s2)   #并集
se.update(s2)  #将s2加到se


#####字典
#键 值
di = {'a':1,'b':2,'a':4}  #difine type 1
d1 = dict(c=3,d=4)  #difine type 2


#查看键值
di['a']  #索引方式 使用  键进行索引键值

#字典键值可以改变  键是唯一
di['a'] = 6

#添加字典key
di['e'] = 7  #直接添加原字典没有的键值


di.fromkeys('abc')  #默认为none
di.fromkeys('abc',1) #添加


di.get('a')  #返回字典中的对应key的值 若没有  none
di.get('w',10)   #返回字典中key对应键值  若没有返回  自赋值 10
a,b = di.get(1,(1,2))  #常用

#keys+values
di.items()
list(di.items())

#keys
di.keys()
list(di.keys())
list(di)

#values
di.values()
list(di.values())

#pop  注意加入keys
di.pop('a')
di.pop('a',4)  #同get

di.popitem()  #删除随机的键值元组
di.setdefault('s',2) #添加键值

di.update({2:50}) #添加键值  内容为字典


#总结
"""
掌握的
字典
get   keys   values

"""

"""
可变对象 ：  list  dict  set
不可变对象： str  tuple  number
"""
