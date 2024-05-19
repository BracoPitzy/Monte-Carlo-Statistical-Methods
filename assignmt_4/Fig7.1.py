"""Monte Carlo Statistical Methods Fig7.1"""
import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

# Assume gamma distribution parameters are a and b
a = 2.0  # Shape parameter
alpha = 2.43
b = 2 / alpha  # Scale parameter

# Convert scale parameter to scale
scale = 1 / b

# Draw 5000 samples from the gamma distribution
samples = gamma.rvs(a=a, scale=scale, size=5000)

"""Accept-Reject Algorithm"""
x_values_AR = []  # Store accepted samples
sum_values_AR = []  # Store cumulative sum
cumulative_sum_AR = 0
m = 0

for y in samples:
    p = np.random.rand()  # Generate a random number between 0 and 1
    py = (np.e * y * np.exp(-y / alpha) / alpha) ** (alpha - int(alpha))
    if p < py:
        x = y
        x_values_AR.append(x)
        cumulative_sum_AR = (cumulative_sum_AR * m + x ** 3) / (m + 1)  # Calculate cumulative sum
        sum_values_AR.append(cumulative_sum_AR)
        m += 1

# Select iteration numbers multiples of 10
x_values_plot_AR = [i for i in range(1, m + 1) if i % 50 == 0]
y_values_plot_AR = [sum_values_AR[i - 1] for i in x_values_plot_AR]

"""Metropolis-Hastings Algorithm"""
x_values_MH = []
sum_values_MH = []
cumulative_sum_MH = 0
rho_values = []
t = 0
x = 0

for y in samples:
    x_t = x
    p = np.random.rand()
    py = 0
    if x_t == 0:
        py = 1
    else:
        py = (y / x_t * np.exp((x_t - y) / alpha)) ** (alpha - int(alpha))
    rho_t = min(py, 1)
    rho_values.append(rho_t)
    if p < rho_t:
        x = y
    else:
        x = x_t
    cumulative_sum_MH = (cumulative_sum_MH * t + x ** 3) / (t + 1)
    sum_values_MH.append(cumulative_sum_MH)
    t += 1

# Select iteration numbers multiples of 10
x_values_plot_MH = [i for i in range(1, t + 1) if i % 50 == 0]
y_values_plot_MH = [sum_values_MH[i - 1] for i in x_values_plot_MH]

# Plot the graph
plt.plot(x_values_plot_AR, y_values_plot_AR, marker='o', label='AR Algorithm', linestyle='-', color='blue')
plt.plot(x_values_plot_MH, y_values_plot_MH, marker='s', label='MH Algorithm', linestyle='-', color='red')
plt.xlabel('Iteration Number')
plt.ylabel('Cumulative Sum')
plt.title('Cumulative Sum over Iterations')
plt.grid(True)
plt.legend()
plt.show()

# Print the final cumulative sum values
print("Final Cumulative Sum of AR:", cumulative_sum_AR)
print("Final Cumulative Sum of MH:", cumulative_sum_MH)
print('rho_values:', rho_values)
