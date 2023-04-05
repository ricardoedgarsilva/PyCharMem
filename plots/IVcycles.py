import matplotlib.pyplot as plt
from PIL import Image
from openpyxl.drawing.image import Image as XLImage
import numpy as np
import time

class Plots:
    def __init__(self):

        plt.ion() #Set interactive mode on
        self.fig, self.ax = plt.subplots(nrows=2, ncols=3)
        self.fig.canvas.manager.set_window_title('Measurement plots') #Add title to the window
        plt.subplots_adjust(wspace=0.4, hspace=0.6) # adjust the spacing between subplots

        #Set axis labels
        self.ax[0,0].set_xlabel('Voltage (V)')
        self.ax[0,0].set_ylabel('Current (A)')
        self.ax[0,1].set_xlabel('Voltage (V)')
        self.ax[0,1].set_ylabel('Current (A)')
        self.ax[0,2].set_xlabel('Resistance (Ω)')
        self.ax[0,2].set_ylabel('Time (s)')
        self.ax[1,0].set_xlabel('Voltage (V)')
        self.ax[1,0].set_ylabel('Resistance (Ω)')
        self.ax[1,1].set_xlabel('Voltage (V)')
        self.ax[1,1].set_ylabel('Resistance (Ω)')
        self.ax[1,2].set_xlabel('Voltage (V)')
        self.ax[1,2].set_ylabel('Time (s)')
    
        #Set axis titles
        self.ax[0,0].set_title('IV Curve Cicle -')
        self.ax[0,1].set_title('IV Curve Cicle +')
        self.ax[0,2].set_title('Resistance vs Time')
        self.ax[1,0].set_title('Resistance Cicle -')
        self.ax[1,1].set_title('Resistance Cicle +')
        self.ax[1,2].set_title('Voltage vs Time')

        #Set plots
        self.cicle_plus,         = self.ax[0,1].plot([],[],'r-o',linewidth=1)
        self.cicle_minus,        = self.ax[0,0].plot([],[],'r-o',linewidth=1)
        self.resistance_plus,    = self.ax[1,1].plot([],[],'r-o',linewidth=1)
        self.resistance_minus,   = self.ax[1,0].plot([],[],'r-o',linewidth=1)
        self.resistance_vs_time, = self.ax[0,2].plot([],[],'r-o',linewidth=1)
        self.voltage_vs_time,    = self.ax[1,2].plot([],[],'r-o',linewidth=1)

        
        #Set initial data
        self.data_cicle_plus = np.zeros((0,2))
        self.data_cicle_minus = np.zeros((0,2))
        self.data_resistance_plus = np.zeros((0,2))
        self.data_resistance_minus = np.zeros((0,2))
        self.data_resistance_vs_time = np.zeros((0,2))
        self.data_voltage_vs_time = np.zeros((0,2))

        plt.draw()
        time.sleep(0.3)

    def add_result(self, result):
        # result = ['Voltage Write[V]','Current Write [A]','Resistance [Ω]',Time [s]]

        if result[0] > 0:
            self.data_cicle_plus = np.append(self.data_cicle_plus, [[result[0], result[1]]], axis=0)
            self.data_resistance_plus = np.append(self.data_resistance_plus, [[result[0], result[2]]],axis=0)

        else:
            self.data_cicle_minus = np.append(self.data_cicle_minus, [[result[0], result[1]]], axis=0)
            self.data_resistance_minus = np.append(self.data_resistance_minus, [[result[0], result[2]]], axis=0)
        
        self.data_resistance_vs_time = np.append(self.data_resistance_vs_time, [[result[2], result[3]]], axis=0)
        self.data_voltage_vs_time = np.append(self.data_voltage_vs_time, [[result[0], result[3]]], axis=0)

    def update(self):
        self.cicle_plus.set_data(self.data_cicle_plus[:,0], self.data_cicle_plus[:,1])
        self.resistance_plus.set_data(self.data_resistance_plus[:,0], self.data_resistance_plus[:,1])
        
        self.cicle_minus.set_data(self.data_cicle_minus[:,0], self.data_cicle_minus[:,1])
        self.resistance_minus.set_data(self.data_resistance_minus[:,0], self.data_resistance_minus[:,1])

        self.resistance_vs_time.set_data(self.data_resistance_vs_time[:,0], self.data_resistance_vs_time[:,1])
        self.voltage_vs_time.set_data(self.data_voltage_vs_time[:,0], self.data_voltage_vs_time[:,1])

        self.ax[0,0].relim()
        self.ax[0,0].autoscale_view()
        self.ax[0,1].relim()
        self.ax[0,1].autoscale_view()
        self.ax[1,0].relim()
        self.ax[1,0].autoscale_view()
        self.ax[1,1].relim()
        self.ax[1,1].autoscale_view()
        self.ax[0,2].relim()
        self.ax[0,2].autoscale_view()
        self.ax[1,2].relim()
        self.ax[1,2].autoscale_view()

        plt.draw()
        plt.pause(0.1)

    def show(self):
        plt.ioff() #Set interactive mode off
        plt.show()

    def clear(self):
        '''Clear the plots'''
        self.data_cicle_plus = np.zeros((0,2))
        self.data_cicle_minus = np.zeros((0,2))
        self.data_resistance_plus = np.zeros((0,2))
        self.data_resistance_minus = np.zeros((0,2))
        plt.draw()

    def image(self):
        '''Return the plot as a PNG image'''
        import io
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image = XLImage(Image.open(buffer))
    
    # Return the PIL Image object
        return image
    
    