"""Monte Carlo Statistical Methods Fig3.7"""
import matplotlib.pyplot as plt
from scipy.stats import t, norm, cauchy  # 导入t分布、正态分布和柯西分布的函数
import numpy as np

# 定义学生分布的参数
df = 12  # 自由度
loc = 0  # 位置参数
scale = 1  # 尺度参数
std_normal = norm(loc=0, scale=1)

# 设定随机种子以确保结果可复现
np.random.seed(0)

# 初始化m的范围
m_values = np.arange(1, 50001, 100)  # 从1到10000

# 初始化f的数组
f_values_uniform = np.zeros_like(m_values, dtype=float)
f_values_t = np.zeros_like(m_values, dtype=float)
f_values_normal = np.zeros_like(m_values, dtype=float)
f_values_cauchy = np.zeros_like(m_values, dtype=float)

# 定义参数a，这是xi服从的均匀分布的上界
a = 1/2.1  # 可以根据需要调整这个值

# 对于每一个m值，生成m个样本并计算f
for i, m in enumerate(m_values):
    # 生成m个服从0到a均匀分布的样本
    samples_uniform = np.random.uniform(0, a, m)
    # 计算每个样本点在学生分布下的密度值
    density_values_uniform = t.pdf(1/samples_uniform, df, loc=loc, scale=scale)
    # 计算f = 累和xj的平方
    f_values_uniform[i] = (np.sum(samples_uniform ** (-7) * density_values_uniform))/(2.1 * m)

    # 生成m个样本xi，xi服从自由度为12的T分布
    samples_t = np.random.standard_t(df=12, size=m)
    # 计算f = 累和(xj的5次方 * I(xj))
    f_t = 0
    for xj in samples_t:
        if xj >= 2.1:
            f_t += (xj ** 5) / m
    f_values_t[i] = f_t

    # 生成m个样本xi，xi服从标准正态分布
    samples_normal = np.random.normal(loc=0, scale=1, size=m)
    # 计算f = 累和(xj的5次方 * I(xj))
    f_normal = 0
    for xj in samples_normal:
        if xj >= 2.1:
            f_normal += (xj ** 5 * t.pdf(xj, df)) / (m * std_normal.pdf(xj))
    f_values_normal[i] = f_normal

    # 生成m个样本xi，xi服从标准柯西分布
    samples_cauchy = cauchy.rvs(size=m)
    # 计算f = 累和(xj的5次方 * I(xj))
    f_cauchy = 0
    for xj in samples_cauchy:
        if xj >= 2.1:
            f_cauchy += (xj ** 5 * t.pdf(xj, df)) / (m * cauchy.pdf(xj))
    f_values_cauchy[i] = f_cauchy

# 绘制f_uniform，f_t，f_normal和f_cauchy关于m的图像
plt.figure(figsize=(10, 5))  # 设置图形大小

# 绘制f_uniform
plt.plot(m_values, f_values_uniform, color='b', label='Uniform', linestyle='--')

# 绘制f_t
plt.plot(m_values, f_values_t, color='r', label='Student\'s t', linestyle='-')

# 绘制f_normal
plt.plot(m_values, f_values_normal, color='g', label='Standard Normal', linestyle='-')

# 绘制f_cauchy
plt.plot(m_values, f_values_cauchy, color='purple', label='Cauchy', linestyle='--')

# 设置坐标轴标签和图例
plt.xlabel('m')
plt.ylabel('f')
plt.title('Fig3.7: Comparison of f values for different distributions')
plt.legend()  # 显示图例
plt.grid(True)

# 设置纵坐标轴范围为0到8
plt.ylim(0, 10)

# 显示图形
plt.show()
