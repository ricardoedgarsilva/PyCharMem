#Creates main handler object
from modules.common import *
from modules.interface import main_menu, measurement_file_menu
import importlib
import numpy as np




class MainHandler:
    def __init__(self,console,logger,config):
        #Create object variables
        self.running = True
        self.console = console
        self.logger = logger
        self.config = config

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

    def main(self):
        while self.running:
            self.main_option = main_menu(self.console)
            
            match self.main_option:
                case 'select_measurement':
                    self.meas_type = measurement_file_menu(self.console,self.logger)

                    module = importlib.import_module(f'modules.measurements.{self.meas_type}')
                    measurement_type = getattr(module, self.meas_type)
                    measurement = measurement_type(self.config, self.console, self.logger)
                    measurement.set_sourcemeter(self.sourcemeter)
                    measurement.measure_cycle(self.sourcemeter)




                case 'check_addresses': print_available_addresses(self.console,self.logger)
                case 'edit_config': edit_config(self.logger)
                case 'exit': self.running = False


