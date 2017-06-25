#第一题
'''
定义一个函数，
输入一个序列，判断序列是顺序还是逆序
顺序输出UP，逆序输出DOWN，否则输出None

逆序之前要先顺序  先sorted  后reversed

'''

a = 'abcd'
b = 'dcba'
c = 'Abcd'
d = 'dcbA'
e = 'sdfaweasd'

f = (1,2,3,34)
g = (34,3,2,1)
h = (2,3,42,1,3)

i = [2,3,4]
l = [4,3,2,1]
m = [3,4,2,1]

li = [1,'a',12]

def func_rank(x):
    if list(x) == list(sorted(x)):
        print('UP')
    elif list(x) == list(reversed(sorted(x))):
        print('Down')
    else:
        print('None')


#第二题  
def sub(seq):
    a = sorted(seq)
    a = list(a)
    #a.reverse()
    #if type(seq) == str:
    if isinstance(seq,str):
        return ''.join(a)
    elif type(seq) == tuple:
        return tuple(a)
    else:
        return a

