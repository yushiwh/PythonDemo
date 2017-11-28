class Car():
    """一次模拟汽车的简单的测试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        """增加一个有初始值的属性"""
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回正解的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("这部车的里程数是-->" + str(self.odometer_reading) + '公里')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你输入的里程数有问题")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


"""继承Car类"""


class EletricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)


"""进行调用"""
my_new_car = Car('audi', 'A4', '2016')
print("我的新车是---->" + my_new_car.get_descriptive_name())

my_tesla = EletricCar('Tesla', 'model_s', 2016)
print(my_tesla.get_descriptive_name())
