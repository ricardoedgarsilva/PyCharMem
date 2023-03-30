import matplotlib.pyplot as plt
import numpy as np

class measurement_plots:
    def __init__(self):

        plt.ion() #Set interactive mode on
        self.fig, self.ax = plt.subplots(nrows=2, ncols=2)
        self.fig.canvas.manager.set_window_title('Measurement plots') #Add title to the window
        plt.subplots_adjust(wspace=0.4, hspace=0.6) # adjust the spacing between subplots

        #Set axis labels
        self.ax[0,0].set_xlabel('Voltage (V)')
        self.ax[0,0].set_ylabel('Current (A)')
        self.ax[0,1].set_xlabel('Voltage (V)')
        self.ax[0,1].set_ylabel('Current (A)')
        self.ax[1,0].set_xlabel('Voltage (V)')
        self.ax[1,0].set_ylabel('Resistance (Ohm)')
        self.ax[1,1].set_xlabel('Voltage (V)')
        self.ax[1,1].set_ylabel('Resistance (Ohm)')
    
        #Set axis titles
        self.ax[0,0].set_title('IV Curve Cicle +')
        self.ax[0,1].set_title('IV Curve Cicle -')
        self.ax[1,0].set_title('Resistance Cicle +')
        self.ax[1,1].set_title('Resistance Cicle -')

        plt.draw()

    def update(self, data):
        # Data is a nested list of the form: [[voltage+, current+, resistance+], [voltage-, current-, resistance-]]

        #Update IV curves
        self.ax[0,0].plot(data[0][0], data[0][1])
        self.ax[0,1].plot(data[1][0], data[1][1])

        #Update resistance curves
        self.ax[1,0].plot(data[0][0], data[0][2])
        self.ax[1,1].plot(data[1][0], data[1][2])
        plt.draw()
        plt.show()
    
    def show(self):
        plt.ioff() #Set interactive mode off
        plt.show()
    




