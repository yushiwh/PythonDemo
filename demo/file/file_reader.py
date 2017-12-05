"""任何方式读取文件，先打开文件"""
"""open在当前执行文件目录中查找对应的文件"""
with open('pi_digits.txt')  as file_object:
    contents = file_object.read()
    print(contents.rstrip())

"""读取文件夹里面的文件"""
with open("text_files\\test.txt")  as file_object1:
    contents1 = file_object1.read()
    print(contents1.rstrip())

"""逐行读取文件"""

print("#################################")
fliename = "pi_digits.txt"
with open(fliename) as file_object:
    for line in file_object:
        print(line.rstrip())


"""将文件存储在一个列表中，外部进行调用"""

print("#################################")
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
