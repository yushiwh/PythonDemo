"""任何方式读取文件，先打开文件"""
"""open在当前执行文件目录中查找对应的文件"""
with open('pi_digits.txt')  as file_object:
    contents = file_object.read()
    print(contents)
