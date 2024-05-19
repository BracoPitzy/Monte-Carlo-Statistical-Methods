import matplotlib.pyplot as plt
from scipy.stats import t
import numpy as np
from scipy.stats import norm

# 定义学生分布的参数
df = 12  # 自由度
loc = 0  # 位置参数
scale = 1  # 尺度参数
std_normal = norm(loc=0, scale=1)

# 设定随机种子以确保结果可复现
np.random.seed(0)

# 初始化m的范围
m_values = np.arange(1, 35001, 100)  # 从1到10000

# 初始化f的数组
f_values3 = np.zeros_like(m_values , dtype=float)

# 定义参数a，这是xi服从的均匀分布的上界
a = 1/2.1  # 你可以根据需要调整这个值

# 对于每一个m值，生成m个样本并计算f
for i, m in enumerate(m_values):
    # 生成m个服从0到a均匀分布的样本
    samples = np.random.uniform(0, a, m)
    # 计算每个样本点在学生分布下的密度值
    density_values = t.pdf(1/samples, df, loc=loc, scale=scale)
    # 计算f = 累和xj的平方
    f_values3[i] = (np.sum(samples ** (-7) * density_values))/(2.1 * m)

# 初始化一个空列表来存储f的值
f_values1 = []

# 循环从0到10000
for m in range(1, 35001, 100):
    # 生成m个样本xi，xi服从自由度为12的T分布
    samples = np.random.standard_t(df=12, size=m)

    # 初始化f的值为0
    f = 0

    # 计算f = 累和(xj的5次方 * I(xj))
    for xj in samples:
        # 判断xj是否大于等于2.1
        if xj >= 2.1:
            # 如果是，则累加到f
            f += (xj ** 5) / m

            # 将f的值添加到列表中
    f_values1.append(f)

f_values4 = []


for m in range(1, 35001, 100):
    # 生成m个样本xi，xi服从自由度为12的T分布
    samples = np.random.normal(loc=0, scale=1, size=m)

    # 初始化f的值为0
    f = 0

    # 计算f = 累和(xj的5次方 * I(xj))
    for xj in samples:
        # 判断xj是否大于等于2.1
        if xj >= 2.1:
            # 如果是，则累加到f
            f += (xj ** 5 * t.pdf(xj, df)) / (m * std_normal.pdf(xj))

            # 将f的值添加到列表中
    f_values4.append(f)


# 绘制f_uniform和f_t关于m的图像
plt.figure(figsize=(10, 5))  # 设置图形大小

# 绘制f_uniform
plt.plot(m_values, f_values3, color='b', label='3', linestyle='--')

# 绘制f_t
plt.plot(m_values, f_values1, color='r', label='1', linestyle='-')
plt.plot(m_values, f_values4, color='g', label='4', linestyle=':')

# 设置坐标轴标签和图例
plt.xlabel('m')
plt.ylabel('f')
plt.title('Fig3.7')
plt.legend()  # 显示图例
plt.grid(True)

# 设置纵坐标轴范围为0到8
plt.ylim(5, 10)

# 显示图形
plt.show()