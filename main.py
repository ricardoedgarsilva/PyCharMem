# Imports
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt
from rich.status import Status
from rich.logging import RichHandler
import logging
import pyvisa
import numpy as np
import time

from modules.interface.main_menu import main_menu
from modules.interface.sel_menu import sel_menu
from modules.common import *
from modules.measurements import *
from art import text2art
install()

logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])


class Main:
    def __init__(self):
        self.running = True
        self.console = Console()
        self.logger = logging.getLogger('rich')
        splash_screen(self.console)

        #Open config
        self.config = load_config(self.logger)
        hide_debug(self.config, self.logger) #Hide debug messages if debug is set to false in config


        #Open Sourcemeter
        try:
            self.rm = pyvisa.ResourceManager()
            self.sourcemeter = self.rm.open_resource(self.config.get('sourcemeter','address'))
            self.logger.info('Sourcemeter found!')
        except:
            self.logger.critical('Sourcemeter not found!')
            quit() 

        self.logger.info('Loading complete!')
        
    
    def main(self):
        while self.running:
            self.main_option = main_menu(self.console)

            match self.main_option:
                case 'select_measurement':
                    self.config = load_config(self.logger)
                    self.meas_type = sel_menu(self.console,self.logger)
                    # ....
                
                case 'check_adresses': print_available_adresses(self.console)
                case 'edit_config': edit_config()
                case 'exit': self.running = False



measurement = Main()
measurement.main()