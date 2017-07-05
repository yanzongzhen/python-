#第二题
'''

2.定义一个矩形的类：
    要求：1.有长和宽的属性
          2.有一个计算面积的方法
          rectangle

'''
class RectShape: #object
    def __init__(self,length,width):
        #判断是否为int数字类型
        if isinstance(length,(int,float)) and isinstance(width,(int,float)):
            self.length = length
            self.width =width
        else:
            return False
    def area(self):
        print('面积为：'+'%d'%(self.length * self.width))

        
shape1 = RectShape(3,2)


#第三题
'''
3.写一个正方形的类，继承矩形类
    要求：有一个判断是不是正方形的方法
'''
class Squera(RectShape):#继承RectShape类
    def judgement(self):
        if self.length == self.width:
            print('这是一个正方形')
        else:
            print('这不符合正方形')

squera = Squera(23,22)

            
    
