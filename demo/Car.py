class Car():
    """一次模拟汽车的简单的测试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回正解的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


"""进行调用"""
my_new_car = Car('audi', 'A4', '2016')
print("我的新车是---->" + my_new_car.get_descriptive_name())
