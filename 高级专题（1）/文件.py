#文件
#open
'''
r 只读模式，文件不存在时会报错。
w 写入模式，文件存在会清空之前的内容，文件不存在则会新建文件。
x 写入模式，文件存在会报错，文件不存在则会新建文件。
a 追加写入模式，不清空之前的文件，直接将写入的内容添加到后面。
b 以二进制模式读写文件，wb,rb,ab。
+ 可读写模式，r+,w+,x+,a+,这几种模式还遵循了r,w,x,a的基本原则。
'''

path = r'D:\python_files\aaa.txt'
file = open(path,'w',encoding = 'utf8')
file.write('aaaaa')
file.close()  #关闭文件
file = open(path,'w',encoding = 'utf8')
file.flush()
a = ['人生苦短，我用python','\n','python是最好的编程语言','测试']

file.write(a[0] + '\n')
file.writelines(a)
file.close()

file = open(path,'r',encoding = 'utf8')
file.read()
file.seek(0,0)
file.readline()
file.close()

file.closed  #判断是否关闭文件
file.mode
file.name

with open(path,'r',encoding = 'utf-8') as f:
    print(f.read())
