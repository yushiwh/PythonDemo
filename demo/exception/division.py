"""使用try-catch进行捕获"""
try:
    print(5 / 1)
except ZeroDivisionError:
    print("除数为0")
else:
    print("没有异常发生")
