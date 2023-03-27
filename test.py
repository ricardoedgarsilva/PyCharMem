import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(nrows=2, ncols=2)


x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)

for i in range(10):
    y = np.sin(x + i/10)
    ax.clear()
    ax.plot(x, y)
    plt.draw()
    plt.pause(0.1)

plt.show()


# Create a matrix of 4x4 plots with matplotlib and update them in a loop
