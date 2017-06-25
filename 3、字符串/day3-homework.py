#第一题


#第二题 如何替换列表中的元素

li = [1,2,'a',4]
li.index('a')
li.insert(2,1)
li.pop(2)

#第三题
a = '苦短'
b = 'Python'
#1
'人生'+a+' 我用'+b
#2
'人生{} 我用{}'.format(a,b)
#3
'人生%s 我用%s'%(a,b)
#4
''.join(['人生',a,',','我用',b])


#第四题
te = 'string test'
te1 = te.replace('test','OK')
print(te1)

#第五题
ls = ['I','like','python']
print(' '.join(ls))
