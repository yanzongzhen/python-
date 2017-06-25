#列表常用的方法

#index 索引  object 对象

#列表的方法全讲 字符串 元组  讲常用

#列表的方法

li = [1, 2, 3, 4, 5, 6, 'a']
"""
TAB自动补全

追加 append(object) 将object加到列表末尾
li.append((1,2,3))
[1, 2, 3, 4, 5, 6, 'a',(1,2,3)]

清空 clear()

复制 copy（）

计数 count(value)

扩展 extend（iterable） 将元素放入列表
li.extend([2,5])
[1, 2, 3, 4, 5, 6, 'a', 2, 2, 5]

index  返回设定范围中第一次出现的位置

插入  L.insert(index, object) -- insert object before index  在索引目标前加object

删除  li.pop([index]) 默认删除栈顶元素 并返回元素

删除  li.remove(value)  删除第一次出现的该value

列表反转排序 li.reverse() 逆序

sort sorted  同类型排序
li.sort(key = none,reverse = flase).......
"""
