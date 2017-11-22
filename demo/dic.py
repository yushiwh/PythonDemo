###字典表的例子####
alien = {'color': 'red',
         'point': '5',
         }
print(alien['color'])
print(alien['point'])
alien['haha'] = 'hahaha'
alien['ok'] = 'ok'
alien['hahaha'] = 'hahaha'
print(alien)

del alien['ok']
print(alien)

for key, value in alien.items():
    print("\nKey:" + key)
    print("Value:" + value)

print('###获取key值######')
for key in alien.keys():
    print(key)

print('###获取value值######')
for value in alien.values():
    print(value)

print('####去除重复的数据########')
for value in set(alien.values()):
    print(value)

var_1 = {'color': 'red', 'point': '50'}
var_2 = {'color': 'green', 'point': '20'}
var_3 = {'color': 'blue', 'point': '10'}
vars = [var_1, var_2, var_3]
for al in vars:
    print(al)

#############随机赋值###########
yy = []
for num in range(10):
    new_al = {'color': 'red', 'point': '50'}
    yy.append(new_al)
print(yy)
print("一共创建了" + str(len(yy)) + "个元素")

##修改其中的三个元素的数据####
for al in yy[0:3]:
    if al['color']== 'red':
        al['color'] = 'yellow'
        al['point'] = 10
print("###修改后的数组####")
print(yy)

