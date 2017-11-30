import car

my_tesla = car.EletricCar('Tesla', 'model_s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

my_battery = car.Battery()
my_battery.describe_battery()
