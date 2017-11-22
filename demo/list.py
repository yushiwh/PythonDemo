bike = ['1', '2', '3']
print(bike)
print(bike[0])
print(bike[-1])

bike[0] = '9'
print(bike)
bike.append('666')
print(bike)
del bike[-1]
print(bike)

card = ['aaa', 'ccc', 'ef', 'df']
card.sort(reverse=True)
print(card)
print(len(card))
##########################################################


for c in card:
    print(c)
    print(c + "hahahaha")
print('OK')

numbers = list(range(1, 6))
print(numbers)

even_num = list(range(2, 11, 2))
print("得到的偶数数组是:" + str(even_num))

squars = []

for value in range(1, 11):
    squar = value ** 2
    squars.append(squar)
print("得到的平方的数组为：" + str(squars))

print("最小的数:" + str(min(squars)))
print("最大的数:" + str(max(squars)))
print("求和的数:" + str(sum(squars)))

squars = [value ** 2 for value in range(1, 11)]
print(squars)

print("数组切片:" + str(squars[0:3]))
print("数组切片:" + str(squars[3:6]))
print("数组切片:" + str(squars[3:-1]))
print("数组切片:" + str(squars[-3:]))

######复制列表########

squars_copy = squars[:]
print("复制过来的列表:" + str(squars_copy))

########元组############
sss = (100, 200)
print(sss[0])
for s in sss:
    print(s)

for ss in squars:
    if ss % 2 == 0:
        print(str(ss) + "是偶数")
    else:
        print(str(ss) + "是奇数")
