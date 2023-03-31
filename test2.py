import numpy as np
import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.x_data = []
        self.y_data = []

    def add_data(self, x, y):
        self.x_data.append(x)
        self.y_data.append(y)

    def update(self):
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        plt.draw()
        plt.pause(0.001)

# create an instance of the plot class
plot = Plot()

# add some data to the plot
for i in range(100):
    x = i/10.0
    y = np.sin(x)
    plot.add_data(x, y)
    plot.update()

# show the final plot
plt.show()
