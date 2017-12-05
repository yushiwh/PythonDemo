"""写入文件"""
filename = "programeming.txt"
"""以写入的模式打开文件   """
"""'r' 读取模式   'w' 写入模式  'a' 附加模式  'r+'读取和写入文件模式  默认只读打开 """
with open(filename, 'w') as file_object:
    file_object.write("I'M yushi.  \n")
    file_object.write("I Love TuTu \n")


"""以附加模式写入文件，不再清空源文件"""
with open(filename,'a') as file_object:
    file_object.write("I Love YuShengHan \n")