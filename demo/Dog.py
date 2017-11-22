##创建类####
class Dog():
    '''下面是类的各种函数'''

    def __init__(self, name, age):
        '''初始化姓名和年纪'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟坐下'''
        print(self.name.title() + "蹲下了")
        return 'site方法'

    def roll_over(self):
        '''模拟打滚'''
        print(self.name.title() + "打滚了")
        return 'roll_over方法'


my_dog = Dog('duoduo', 6)
you_dog = Dog('YYYY', 8)
print("我的狗狗的名字是:" + my_dog.name.title())
print("我狗狗的年纪是:" + str(my_dog.age) + "岁")
print("调用方法:" + str(my_dog.sit()))
print("调用方法:" + str(my_dog.roll_over()))

print("你的狗狗的名字是:" + you_dog.name.title())
print("我狗狗的年纪是:" + str(you_dog.age) + "岁")
print("调用方法:" + str(you_dog.sit()))
print("调用方法:" + str(you_dog.roll_over()))

