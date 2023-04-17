import sys
import random
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('PyQtGraph Plots')
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        # Create the plots
        self.plots = []
        for i in range(3):
            for j in range(3):
                plot = pg.PlotWidget()
                plot.setTitle(f'Plot {i+1}-{j+1}')
                plot.showGrid(x=True, y=True)
                layout.addWidget(plot, i, j)
                self.plots.append(plot)

        # Set up the timer to update the plots
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plots)
        self.timer.start(100)  # update every 100 ms

        # Set up the data
        self.data = [[] for _ in range(9)]
        self.x = 0

    def update_plots(self):
        # Add a new datapoint to each plot
        for i, plot in enumerate(self.plots):
            self.data[i].append(random.uniform(0, 1))
            plot.plot(self.data[i], pen='b', clear=True)
            plot.plot([self.x, self.x], [0, 1], pen='r')
        self.x += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
