#列表方法
li = [2,3,4,5,6]

#字符串
s = 'hello'
t = 'python'
r = '!'
f = '人生苦短 我用python'
b = 'this is string test'
b.count('t')  #计数 有区间
b.endswith('t')  #判断以什么结尾  返回布尔类型 有区间
b.startswith('t')  #判断是否以传入值为开始  返回布尔类型 有区间

#python3使用的时UTF-8

b.find('a')   #返回此字符在第一次出现的位置  否则返回-1  有区间
b.index('t')#同上  但若没有找到报错  有区间


c = 'abcdefg'
c.isalpha()   #判断是的都时字符  是->true    else....
d = '12334'
d.isdigit()   #判断是否都是数字  返回布尔值
c.upper()  #将小写字符转成大写
e = 'ABCDEFG'
#列表可变序列，字符串和元祖为不可变序列
e.lower()  #将大写字幕转化小写

b.replace('t','T',2)  #S.replace(old, new[, count]) -> str  count转换的位数
b.split()  #分割成列表 默认一空格分割 传参数后以参数去分割
b.split('i')
b.split('i',1)

#字符串的拼接
#方法一  利用+号进行拼接  必须为同类型

s + t + r
s + ' ' + t +' ' + r

#方法2  格式化字符串 %s
'%s %s %s'%(s,t,r)

#3 join
' '.join([s,t,r])  #join   S.join(iterable) -> str

#4 format
'{} {} {}'.format(s,t,r)
'{0} {1} {2}'.format(s,t,r)
'{2} {1} {0}'.format(s,t,r)
'{n0} {n1} {n2}'.format(n2=s,n0=t,n1=r)

#格式化 
'%d'%123      #格式化整形 %d
'%.2f'%2.333  #格式化浮点型  %.2f  %5.2f
'%c'%61       #格式化ASCII码
'%o'%8        #格式化8进制
'%x'%16       #格式化16进制
'%e'%10.23    #格式化科学计数法

#  '%m.nf'  m为从右向左数m位不足用空格补  m为证右对齐  m为负右对齐   n表示小数保留位数
'%7.2f'%2.3 #左对齐
'%-7.2f'%2.3#右对齐
'%7.2f'%2.3  #用0填充空格
'%+7.2f'%2.3 #正数前面添加正号
'%0+7.2f'%2.3
'%-+7.2f'%2.3

'%5s'%'ab'
'%-5s'%'ab'


#转义
e = """python
"""
"""
\ 是转义符
\n  换行
\a  提示音
\t  tab  横向制表符
\b  退格符
\r  回车键
\f  换页

"""
print('\a')
print('xyz\tmn')
print('xyz\bmn')
print('xyz\rmn')
print('xyz\fmn')

g = 'abcd\'bgfg\'efg'
h = "abdf'agg'agagf"




