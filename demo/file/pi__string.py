"""读取使用文件，赋值到字符串里面去"""
print("#################################")
filename = "pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
"""处理多的数据"""
print(pi_string[:22]+"...")





