import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.random.randint(1, 50, 15)
y = np.random.randint(1, 50, 15)
sizes = np.random.randint(100, 1000, 15)  # bubble size
colors = np.random.rand(15)  # different colors

# Bubble plot
plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.6, edgecolors='black')

plt.title("Bubble Plot with Different Colors")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.colorbar(label="Color Scale")

plt.show()