# Imports ---------------------------------------------------------------------
import os
import sys
import logging
import platform
import datetime
import configparser
import pyvisa
from art import text2art
from rich.console import Console
from rich.traceback import install
from rich.logging import RichHandler
from rich.panel import Panel
from rich.prompt import Prompt
from rich.status import Status
# -----------------------------------------------------------------------------

install()
console = Console()
logger = console.logger


#Common functions -------------------------------------------------------------
def verbose_debug(verbose: bool):
    """Verbose Debug"""
    # Verbose Debug
    if verbose:
        logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    else:
        logging.basicConfig(level='INFO', format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])

    return logging.getLogger("rich")

def clear_terminal():
    """Clear Terminal"""
    os.system('cls||clear')

def printnewlines(lines: int):
    """Print New Lines"""
    print(lines*"\n")

def splash_screen(console: Console):
    """Splash Screen"""
    info = configparser.ConfigParser()
    info.read(os.path.join('modules','info.ini'))
    print(text2art(info.get('main','name')))
    console.print(f"Version: {info.get('main','version')}",style='bold blue')
    console.print(f"Author: {info.get('main','author')}",style='bold blue')
    printnewlines(5)

def config_open(logger: logging.Logger):
    """Open the config file"""
    try:
        match platform.system():
            case 'Windows': os.system(f'start config.ini')
            case 'Darwin':  os.system(f"open config.ini")
            case 'Linux':   os.system(f"open config.ini")
    except:
        logger.critical('Config file not found')
        quit()

def config_read(logger: logging.Logger):
    """Read the config file"""
    try:
        return configparser.ConfigParser().read('config.ini')
    except:
        logger.critical('Config file not found')
        quit()

def path_exists(path: str):
    """Check if path exists"""
    return os.path.exists(path)

def get_path():
    """Get the path to the file"""
    path = os.path.dirname(os.path.realpath(__file__))
    return path[:path.rfind('\\')]

def mkdir(logger: logging.Logger, path: str):
    '''Creates the path if it doesn't exist'''
    if path_exists(path): 
        logger.debug(f'Folder {path} already exists')
    else: 
        os.makedirs(path)
        logger.debug(f'Folder {path} created')

def get_index(path: str):
    '''Returns the index of the file in the folder'''
    return len(os.listdir(path))

def get_filename(path: str ,sample: str, device: str):
    '''Returns the filename with the date_sample_device_index.xlsx format'''
    index = get_index(path)
    date = datetime.datetime.now().strftime('%Y%m%d')
    return f'{date}_{sample}_{device}_{index}.xlsx'

def print_available_addresses(logger: logging.Logger, console: Console):
    '''Prints the available adresses'''
    rm = pyvisa.ResourceManager()
    addresses = rm.list_resources()
    printnewlines(1)

    console.print(Panel.fit("[bold]Available Addresses[/bold]", border_style="green"))    
    if len(addresses) == 0: logger.critical('No addresses found!')
    else:
        for address in addresses:
            console.print(address)

def check_missing_params(logger: logging.Logger, my_dict: dict, my_list: list):
    '''Checks if the dictionary has all the keys in the list'''
    
    missing_items = [item for item in my_list if item not in my_dict]

    if len(missing_items) == 0: logger.info('All measurement parameters found!')
    else:
        logger.critical('Missing measurement parameters:')
        for item in missing_items:
            logger.critical(f'- {item}')
        quit()






