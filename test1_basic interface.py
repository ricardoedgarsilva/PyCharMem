from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication,QMainWindow, QStyleFactory, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QTabWidget, QGridLayout
import sys, random
import pyqtgraph as pg

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCharMem")
        self.setGeometry(100, 100, 600, 400)

        # Create a tab widget
        self.tab_widget = QTabWidget(self)

        # Create
        #  a QWidget to hold the plots for the "Plots" tab        
        plot_tab = QWidget()
        plot_layout = QVBoxLayout(plot_tab)
        plot_grid = QGridLayout()
        for row in range(3):
            for col in range(3):
                plot_widget = pg.PlotWidget()
                plot_widget.setTitle(f"Plot {row*3+col+1}")
                plot_widget.setLabel('bottom', 'X Label')
                plot_widget.setLabel('left', 'Y Label')
                plot_grid.addWidget(plot_widget, row, col)
        plot_layout.addLayout(plot_grid)
        plot_tab.setLayout(plot_layout)
        self.tab_widget.addTab(plot_tab, "Plots")

        # Create a QWidget to hold the table for the "Data" tab
        data_tab = QWidget()
        data_layout = QVBoxLayout(data_tab)
        self.data_table = QTableWidget()
        self.data_table.setRowCount(0) # Start with an empty table
        self.data_table.setColumnCount(3)
        header_labels = ['Line', 'Column 1', 'Column 2']
        self.data_table.setHorizontalHeaderLabels(header_labels)
        data_layout.addWidget(self.data_table)
        data_tab.setLayout(data_layout)
        self.tab_widget.addTab(data_tab, "Data")


        self.setCentralWidget(self.tab_widget)

        for i in range(100):
            self.add_row()



    def add_row(self):
            # Add a new row to the beginning of the table
            self.data_table.insertRow(0)

            # Fill the row with sample data
            for col in range(3):
                item = QTableWidgetItem(f"Row 0, Col {col}")
                self.data_table.setItem(0, col, item)

            # Fill the rows of each plot with random data
            for plot_index in range(9):
                plot_widget = self.tab_widget.widget().layout().itemAt(plot_index).widget()
                plot_widget.plot([random.random() for i in range(10)], pen='r')
                plot_widget.plot([random.random() for i in range(10)], pen='g')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    app.setStyleSheet("QMainWindow::title {background-color: #333333;}")
    window = MyApp()
    window.show()
    app.exec()



