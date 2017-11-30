from car import Car

"""进行调用"""
my_new_car = Car('audi', 'A4', '2016')
print("我的新车是---->" + my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 22;
my_new_car.read_odometer()
