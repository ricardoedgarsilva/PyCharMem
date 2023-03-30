#Creates main handler object
from modules.common import *
from modules.interface import menu, measurement_plots
import importlib
import numpy as np




class MainHandler:
    def __init__(self,console,logger,config):
        #Create object variables
        self.running = True
        self.console = console
        self.logger = logger
        self.config = config
        self.data = np.array([])
        #Splash screen
        clear_terminal()
        splash_screen(console)

        ##Open Sourcemeter
        #model = config.get('sourcemeter','model')
        #srcmtr_file = importlib.import_module(f'modules.sourcemeters.{model}')
        #srcmtr_class = getattr(srcmtr_file, model)
        #self.sourcemeter = srcmtr_class(self.logger,self.config)


        #Sucefully loaded
        self.logger.info('Loading complete!')
        print_available_addresses(self.console,self.logger)


    def main(self):
        while self.running:
            self.main_option = menu('main',self.console,self.logger)
    
            match self.main_option:
                case 'Exit': self.running = False
                
                case 'Print Available Addresses': print_available_addresses(self.console,self.logger)
                
                case 'Edit Configuration': config_edit(self.logger)
                
                case 'Select Measurement':
                    self.config = config_load(self.logger)
                    self.meas_type = menu('measurements',self.console,self.logger)

                    if self.meas_type == 'Back': continue

                    module = importlib.import_module(f'modules.measurements.{self.meas_type}')
                    measurement_type = getattr(module, self.meas_type)
                    measurement = measurement_type(self.config, self.console, self.logger)
                    measurement.set_sourcemeter(self.sourcemeter)

                    plots = measurement_plots()
                    n_cycles = measurement.n_cycle
                    #save_config(self.config,self.logger)


                    measurement.measure_cycle(self.sourcemeter)
                    self.data.concat(measurement.result)


                


