#数据类型 数据结构 课后作业答案

#第一题  定义每种数据类型
a = 1 #整形
b = 1.1 #浮点型
c = True #布尔型
d = False
e = 1 + 2j #复数 
f = set('adbe')  #集合


#第二题答案 创建每种序列类型
li = [1,2,3,4,5,'a']  #列表
tu = (1,2,3)   #元组
l = '这是我的作业 python' #字符串

#第三题答案  对一个长度为5的列表，用多种方法取第3位的值
l2 = [1,2,3,4,5]
#方法一  利用切片
print(l2[2:3])
#方法二
print(l2[2])
#方法三
print(l2[-3])

#第四题答案  有个时间形式是（20170608），通过除法和取余，来得到对应的日，月，年
data = 20170608  #定义时间
day = data%100  #取出日
month = (data%2017)//100 #取出月 (data//100)%100
year = data//10000 #取出年
print(year,'年',month,'月',day,'日')

#第五题答案  怎样向上取整
#方法一 
import math
up = math.ceil(205/20)
print(up)

#方法二
#up = (A+B-1)/B
up1 = (205+20-1)/20
print(int(up1))

#附加题  为什么下标从0 开始
#为了美观

#pop又返回值  remove没有返回值
"""
pop是删除某个位置上的元素并返回删除的元素
remove是删除具体位于列表中的元素不追究位置

"""



