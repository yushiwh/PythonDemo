# 画一个平方数的折线图
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_value = [1, 2, 3, 4, 5]
plt.plot(input_value, squares, linewidth=5)

# 设置图表标题，并且给坐标轴加上标签
plt.title("squares number", fontsize=24)
plt.xlabel("squares", fontsize=24)
plt.ylabel("values", fontsize=24)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=24)
plt.show()
