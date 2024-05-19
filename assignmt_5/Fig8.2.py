"""包尔康2021141210003 蒙特卡罗第五次上机模拟作业Fig8.2"""
import numpy as np
import matplotlib.pyplot as plt

x = 0.25
X_values = [x]
n = 10
p_values = [(x, 0)]  # Initial point (x, u), where u = 0

def f(x):
    return np.exp(- (x + 3) ** 2 / 2)

# Iterating to generate points using the Metropolis-Hastings algorithm
for i in range(n):
    U = np.random.rand()
    u = U * f(x)  # Generating a proposal u
    p_values.append((x, u))  # Appending the proposed point (x, u)
    A = min(1, -3 + np.sqrt(-2 * np.log(u)))  # Acceptance probability
    U2 = np.random.rand()
    x = U2 * A  # Generating the next point based on acceptance probability
    X_values.append(x)
    p_values.append((x, u))  # Appending the accepted point (x, u)

x_f = np.linspace(0, 1, 1000)  # Generating 1000 uniformly distributed x values between 0 and 1
y_f = f(x_f)  # Calculating corresponding y values
x_values, y_values = zip(*p_values)

# Plotting using matplotlib with adjusted colors
plt.figure()  # Creating a new figure

plt.plot(x_f, y_f, label='f(x)', color='blue')  # Plotting f(x) with green color
plt.fill_between(x_f, y_f, color='gray', alpha=0.3)  # Shading area below the curve
plt.plot(x_values, y_values, marker='o', color='red')  # Plotting the points with blue color
plt.legend()
plt.xlabel('X')  # Setting x-axis label
plt.ylabel('Y')  # Setting y-axis label
plt.title('Metropolis-Hastings Sampling')  # Setting the title
plt.grid(True)  # Showing grid
plt.show()  # Displaying the plot
