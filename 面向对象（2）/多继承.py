#1、多继承
'''
当继承的类有同种方法的时候，只会继承前面一个的方法
'''
class Base:
    def play(self):
        print('this is Base')

class A(Base):
    def play(self):
        print('this is A')

class B(Base):
    def play(self):
        print('this is B')

class C(A,B): #s谁在前先继承谁
    #pass
    def play(self):
        super().play() # super(C,self).play()
        print('this is C')

a = C()  #实例化


#2、类的特殊方法
class Rectangle:
    '这是一个矩形类'
    def __init__(self,length,width):
        if isinstance(length,(int,float)) and isinstance(width,(int,float)):
            self.length = length
            self.width  = width
        else:
            raise TypeError
            #return None
    def area(self):
        areas = self.length * self.width
        return areas

    def __str__(self): #利用print返回这个对象
        return '宽为%s,高为%s'%(self.width,self.length)
    def __repr__(self):#直接返回这个对象  优先级大于  str
        return '面积:%s'%(self.area()) 
    def __call__(self):  #实例可被调用
        return 'this is call'
    def __add__(self,other): #作为元组相加  对象相加
        add_length = self.length + other.length
        add_width = self.width + other.width
        return add_length,add_width

b = Rectangle(3,5)
b.__dict__  #返回新的字典   属性为键  值
b.__doc__  #文本文档  注释
c = Rectangle(1,4)

#print(b)
b
b()  #直接调用b()
'''
运算符方法
    __add__(self,other)     x+y
    __sub__(self,other)     x-y 
    __mul__(self,other)     x*y  
    __mod__(self,other)    x%y
    __iadd__(self,other)    x+=y
    __isub__(self,other)    x-=y 
    __radd__(self,other)    y+x
    __rsub__(self,other)     y-x 
    __imul__(self,other)    x*=y 
    __imod__(self,other)    x%=y

'''

