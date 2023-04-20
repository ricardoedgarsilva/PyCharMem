# Imports 
import numpy as np #Necessary for returning nan values

class Measurement:
    def __init__(self, logger, config, instrument): #Initialize measurement (DON'T CHANGE ARGUMENTS)
        # Necessary parameters
        self.name = 'Name of measurement'   # Name of measurement
        self.nparams = ['n_cycles']         # List of necessary parameters
        self.headers = ['Example header']   # List of headers for table and xlsx file
        self.params = dict(config.items())  # Retrieve list of parameters from config file
        self.vals = ['Example value']       # List of values that vary in each measurement
        # End of necessary parameters

        self.set_plot_parameters()                      # Set plot parameters
        self.initialize_instrument(logger, instrument)  # Initialize instrument
        

    def set_plot_parameters(self, cycle_type): # Set plot parameters
        self.plot_grid = (1, 1) # Set plot grid (rows, columns)
        self.plot_titles = [['Example plot title']] # List of plot titles (each list is a row)
        self.plot_labels = [[['Example x label', 'Example y label']]] # List of plot labels (each list is a row, and each plot requires a list with x and y labels)
        self.plot_clear = [[True]] # List of plot clear flags (each list is a row, and each plot requires a boolean value)

    def initialize_instrument(self, logger, instrument):
        # Use this function to initialize the instrument and set its initial parameters, this function is called only once
        logger.debug('Setting instrument initial parameters')
        instrument.reset(logger)
        instrument.write(logger, 'INIT:IMM')
        logger.debug('Instrument parameters set!')

    def measure_val(self, logger, instrument, val):
        # Use this function to measure a single value from the vals list
        # This function is called for each value in the vals list
        # The function should return a list with the results of the measurement and a list with the results of the plots
        # The results of the measurement should be a list of values equal to the specified headers



        # Do something

        # Return results
        result = ['Example value'] # List of results of the measurement
        result_plots = [[['Example x value', 'Example y value']]] # List of results of the plots (each list is a row, and each plot requires a list with x and y values)
        
        return [result, result_plots] # Return results, don't change this line
 
