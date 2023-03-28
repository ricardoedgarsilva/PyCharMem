#Creates main handler object
from modules.common_utils import *
from modules.interface.main_menu import main_menu
from modules.interface.measurement_file_menu import measurement_file_menu
import pyvisa
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

        #Open Sourcemeter
        # try:
        #     self.rm = pyvisa.ResourceManager()
        #     self.sourcemeter = self.rm.open_resource(self.config.get('sourcemeter','address'))
        #     self.logger.info('Sourcemeter found!')
        # except:
        #     self.logger.critical('Sourcemeter not found!')
        #     quit() 

        #Sucefully loaded
        self.logger.info('Loading complete!')

    def main(self):
        while self.running:
            self.main_option = main_menu(self.console)
            
            match self.main_option:
                case 'select_measurement':
                    self.meas_type = measurement_file_menu(self.console,self.logger)
                    # ... some code
                case 'check_addresses': print_available_addresses(self.console,self.logger)
                case 'edit_config': edit_config(self.logger)
                case 'exit': self.running = False


