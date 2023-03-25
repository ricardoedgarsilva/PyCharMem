#Imports
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt
import pyvisa
import numpy as np
import time

from modules.interface.main_menu import main_menu
from modules.interface.measurement_selection_menu import measurement_selection_menu
from modules.basic import *
from modules.measurements import *

running = True
load_config() # Load configuration file

console = Console()
install()


# open sourcemeter
#rm = pyvisa.ResourceManager()
#sourcemeter = rm.open_resource(config.get('sourcemeter','address'))

while running:

    clear_terminal()
    main_menu_selection = main_menu(console)

    match main_menu_selection:
        case 0:
            measurement = measurement_selection_menu(console)
            bar = getattr(measurement, f'measure_{measurement}')
            result = bar()

        case 1:
            edit_config()
            load_config()
        case 2:
            running = False
