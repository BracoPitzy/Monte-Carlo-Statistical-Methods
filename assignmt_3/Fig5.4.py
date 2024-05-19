"""Monte Carlo Statistical Methods Fig5.4"""
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, exp, log

# 定义目标函数 h(x)
def h(x):
    return (cos(50 * x) + sin(20 * x)) ** 2

# 初始参数设置
# x = np.random.uniform(0, 1)  # 从区间 [0, 1] 随机选择初始x值
x = 0
r = 0.5  # 邻域半径
iterations = 2500  # 迭代次数
trajectory = []  # 存储每次迭代的(x, h(x))用于绘图

# 进行迭代
for t in range(1, iterations + 1):
    T_t = 1 / log(t + 1)  # 温度函数
    a_t = max(x - r, 0)  # 确定邻域下界
    b_t = min(x + r, 1)  # 确定邻域上界
    u = np.random.uniform(a_t, b_t)  # 在邻域中随机选择新的x值
    h_x = h(x)
    h_u = h(u)

    # 接受概率
    p_t = min(exp((h_u - h_x) / T_t), 1)
    if np.random.rand() < p_t:
        x = u  # 接受新解

    # 记录当前解
    trajectory.append((x, h(x)))

    # # 每几次迭代绘制一次轨迹图
    # if t % 500 == 0:
    #     xs, hs = zip(*trajectory)
    #     plt.figure(figsize=(10, 5))
    #     plt.plot(xs, hs, marker='o', markersize=2, linestyle='-')
    #     plt.title(f"Iteration: {t}")
    #     plt.xlabel("x")
    #     plt.ylabel("h(x)")
    #     plt.grid(True)
    #     plt.show()

# 绘制最终的轨迹图
xs, hs = zip(*trajectory)
plt.figure(figsize=(10, 5))
plt.plot(xs, hs, marker='o', markersize=3, linestyle='-')
plt.title("Fig 5.4 Simulated Annealing Maximization Iteration Trajectory")
plt.xlabel("Exploration x")
plt.ylabel("Function Value h(x)")
plt.xlim(0, 1)
plt.grid(True)
plt.show()
