"""包尔康2021141210003 蒙特卡罗第二次上机模拟作业Fig4.5"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# 定义学生分布的参数
df = 4.6  # 自由度
loc = 0  # 位置参数
scale = 1  # 尺度参数

# 设定随机种子以确保结果可复现
np.random.seed(0)

# 初始化m的范围
m_values = np.arange(1, 25000, 100)
# m_values2 = np.arange(1, 20000, 200)
f_values_t = np.zeros_like(m_values, dtype=float)
f_values_cond = np.zeros_like(m_values, dtype=float)

# 对于每一个m值，生成m个样本并计算f
for i, m in enumerate(m_values):
    # 生成m个样本xi，xi服从自由度为4.6的标准T分布
    samples_t = np.random.standard_t(df=df, size = m)
    # 计算累和
    f_t = 0
    for xj in samples_t:
        f_t += np.exp(-xj ** 2) / m
    f_values_t[i] = f_t

    samples_gamma = stats.invgamma.rvs(a = df/2, scale = df/2, size = m)
    cond = 0
    for yj in samples_gamma:
        cond += 1 / (m * ((2 * yj + 1) ** 0.5))
    f_values_cond[i] = cond


# 绘制f_t关于m的图像
plt.figure(figsize=(10, 5))  # 设置图形大小
# 生成x坐标的数据
x = np.linspace(0, 20000, 2)
# 生成y坐标的数据，全部为0.5373
y = np.full_like(x, 0.5373)
# 绘制f_t
plt.plot(m_values, f_values_t, color='r', label='X ~ Student\'s t', linestyle='-')

plt.plot(m_values, f_values_cond, color='b', label='X | y ~ N', linestyle='-')

# plt.plot(x , y, color='g', label='accurate', linestyle='--')

# 设置坐标轴标签和图例
plt.xlabel('m')
plt.ylabel('E')
plt.title('Fig4.5: Exp(-x^2)')
plt.legend()  # 显示图例
plt.grid(True)

# 设置纵坐标轴范围为0到8
plt.ylim(0.5, 0.58)
# plt.ylim(0.5, 0.83)

# 设置分辨率
plt.savefig('fig4.5.png', dpi=300)

# 显示图形
plt.show()
