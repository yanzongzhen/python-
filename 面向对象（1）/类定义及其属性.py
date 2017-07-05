#python 的面向对象
a = 'aaa'
type(a)



#类的定义
class Animal:
    #pass
    '''animal class '''
    eye = 2  #类属性
    leg = [] 
    def __init__(self,name,food,color = 'yellow'):  #__init__类的初始化  最先执行  self  默认不带参数  
        self.name = name
        #self.food = food
        self._food = food
        #self.color = color
        self.__color = color
    def play(self):
        print('打豆豆')
    def get_name(self):
        print('%s'%self.name)
        

#实例化对象  小黄人
minions  = Animal('minions','banana')  #实例化
#self.name = minions.name

dog = Animal('旺财','bone')

#类属性
minions.leg.append(2)
dog.leg.append(4)

#实例属性
#dog.color = 'red'

###实例的属性相当于实例自己  类属性是共有的

#类的私有属性

#一个_
#dog._food

#两个__
dog._Animal__color
dog._Animal__color = 'red'

#更多的是一种规范/约定，不没有真正达到限制的目的  最好不要去改私有属性


#继承

class People(Animal):  #继承
    #pass
    #多态
    def __init__(self,weight):  #覆盖已继承的弗雷初始化函数
        self.weight = weight
    def play(self):
        #Animal.play(self)
        super().play()  #继承
        print('papapa')
        

jack = People(57)

#jack.play()

"""
总结：
1.类的定义
2.类的属性和方法
3.类的实例
4.类继承
"""

