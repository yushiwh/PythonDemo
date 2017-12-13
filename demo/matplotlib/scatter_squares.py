# 绘制散点图病设置其样式
import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]

# plt.scatter(x_value, y_value, c=(0, 0, 0.8), edgecolors='none', s=40)
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, edgecolors='none', s=40)

# 设置图表标题并且给坐标轴加上标签
plt.title("squar numbers", fontsize=24)
plt.xlabel("value", fontsize=24)
plt.ylabel("square of values", fontsize=24)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])



# 自动保存图表  bbox_inches裁剪多余的空白区域
plt.savefig('我的图表', bbox_inches='tight')


plt.show()
