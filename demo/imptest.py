###导入函数####
import pizza
import pizza as p

###导入特定的函数###
from pizza import make_pizza
###别名####
from pizza import make_pizza as mp

##调用函数##
pizza.make_pizza(16, '馅料1')
pizza.make_pizza(18, '馅料1', '馅料2')

p.make_pizza(16, '馅料1')
p.make_pizza(18, '馅料1', '馅料2')

make_pizza(16, '馅料1')
make_pizza(18, '馅料1', '馅料2')

mp(16, '馅料1')
mp(18, '馅料1', '馅料2')
