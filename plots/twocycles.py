import matplotlib.pyplot as plt
import numpy as np

class Plots:
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
        self.ax[0,0].set_title('IV Curve Cicle -')
        self.ax[0,1].set_title('IV Curve Cicle +')
        self.ax[1,0].set_title('Resistance Cicle -')
        self.ax[1,1].set_title('Resistance Cicle +')

        #Set plots
        self.cicle_plus,         = self.ax[0,1].plot([],[],'r-o',linewidth=1)
        self.cicle_minus,        = self.ax[0,0].plot([],[],'r-o',linewidth=1)
        self.resistance_plus,    = self.ax[1,1].plot([],[],'r-o',linewidth=1)
        self.resistance_minus,   = self.ax[1,0].plot([],[],'r-o',linewidth=1)

        
        #Set initial data
        self.data_cicle_plus = np.zeros((0,2))
        self.data_cicle_minus = np.zeros((0,2))
        self.data_resistance_plus = np.zeros((0,2))
        self.data_resistance_minus = np.zeros((0,2))

    def add_result(self, result):
        # ['Voltage Write[V]','Current Write [A]','Resistance [Ω]']]

        if result[0] > 0:
            self.data_cicle_plus = np.append(self.data_cicle_plus, [[result[0], result[1]]], axis=0)
            self.data_resistance_plus = np.append(self.data_resistance_plus, [[result[0], result[2]]],axis=0)

        else:
            self.data_cicle_minus = np.append(self.data_cicle_minus, [result[0], result[1]], axis=0)
            self.data_resistance_minus = np.append(self.data_resistance_minus, [result[0], result[2]], axis=0)



    
    def update(self):
        self.cicle_plus.set_data(self.data_cicle_plus[:,0], self.data_cicle_plus[:,1])
        self.resistance_plus.set_data(self.data_resistance_plus[:,0], self.data_resistance_plus[:,1])
        
        self.cicle_minus.set_data(self.data_cicle_minus[:,0], self.data_cicle_minus[:,1])
        self.resistance_minus.set_data(self.data_resistance_minus[:,0], self.data_resistance_minus[:,1])

        self.ax[0,0].relim()
        self.ax[0,0].autoscale_view()
        self.ax[0,1].relim()
        self.ax[0,1].autoscale_view()
        self.ax[1,0].relim()
        self.ax[1,0].autoscale_view()
        self.ax[1,1].relim()
        self.ax[1,1].autoscale_view()

        plt.draw()
        plt.pause(0.1)

    
    def show(self):
        plt.ioff() #Set interactive mode off
        plt.show()
    