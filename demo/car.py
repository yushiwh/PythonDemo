"""一个可用于标识汽车的类"""


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
        """初始化电动车的特有属性"""
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("电瓶的容量是:" + str(self.battery_size))


class Battery():
    """模拟一次电动车电瓶的尝试"""

    def __init__(self, battery_size=60):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("这是描述电瓶-->" + str(self.battery_size) + "的信息")

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "这个车的续航里程为--->" + str(range)
        message += "公里"
        print(message)
