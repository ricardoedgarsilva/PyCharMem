#File with common functions for the project
#Path: modules\common_utils.py

def verbose_debug(verbose):
    '''Hides the debug messages'''
    from rich.logging import RichHandler
    import logging
    if verbose:
        logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    else:
        logging.basicConfig(level='INFO', format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])

    return logging.getLogger("rich")

def clear_terminal():
    '''Clears the terminal'''
    import os
    os.system('cls||clear')

def printnewlines(n):
    '''Prints a new line'''
    print(n*'\n')

def splash_screen(console):
    '''Prints the splash screen'''
    import os
    import configparser
    from art import text2art
    path = os.path.join('modules','info.ini')
    info = configparser.ConfigParser()
    info.read(path)
    print(info.sections())
    print(text2art(info.get('main','name')))
    console.print(f"Version: {info.get('main','version')}",style='bold blue')
    console.print(f"Author: {info.get('main','author')}",style='bold blue')
    printnewlines(5)

def config_edit(logger):
    '''Open the config file in the default editor'''
    import os
    import platform
    filename = 'config.ini'
    
    try:
        match platform.system():
            case 'Windows': os.system(f'start {filename}')
            case 'Darwin':  os.system(f"open {filename}")
            case 'Linux':   os.system(f"open {filename}")
    except:
        logger.critical('Config file not found')
        quit()

def config_load(logger):
    '''Loads the config file'''
    import configparser
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        logger.info('Config file loaded')
        return config
    except:
        logger.critical('Config file not found')
        quit()

def path_exists(path):
    '''Checks if a path exists'''
    import os
    return os.path.exists(path)

def get_path():
    '''Returns the path to the folder where the code is saved'''
    import os
    path = os.path.dirname(os.path.realpath(__file__))
    return path[:path.rfind('\\')]

def folder_path(sample,device):
    '''Returns the path to the folder where the data is saved'''''
    return get_path() + f'\\data\\{sample}\\{device}\\'

def mkdir(logger,path):
    '''Creates the path if it doesn't exist'''
    import os
    if path_exists(path): 
        logger.info(f'Folder {path} already exists')
        pass
    else: 
        os.makedirs(path)
        logger.info(f'Folder {path} created')

def get_index(path):
    '''Returns the index of the file in the folder'''
    import os
    files = os.listdir(path)
    index = len(files)
    return index

def get_filename(path,sample,device):
    '''Returns the filename with the date_sample_device_index.xlsx format'''
    import datetime
    index = get_index(path)
    date = datetime.datetime.now().strftime('%Y%m%d')
    return f'{date}_{sample}_{device}_{index}.xlsx'

def print_available_addresses(logger,console):
    '''Prints the available adresses'''
    import pyvisa
    from rich.panel import Panel
    from modules.common import printnewlines

    rm = pyvisa.ResourceManager()
    printnewlines(1)
    console.print(Panel.fit("[bold]Available Addresses[/bold]", border_style="green"))
    for address in rm.list_resources():
        console.print(address)
    
    if len(rm.list_resources()) == 0:
        logger.critical('No addresses found!')

def check_missing_params(logger,my_dict, my_list):
    '''Checks if the dictionary has all the keys in the list'''
    
    missing_items = [item for item in my_list if item not in my_dict]

    if len(missing_items) == 0:
        logger.info('All parameters found!')
    else:
        logger.critical('Missing parameters:')
        for item in missing_items:
            logger.critical(f'- {item}')
        quit()

def create_list(logger,cycle,max,min,step):
    '''Creates a list of values'''
    import numpy as np

    list1 = np.arange(0,max,step)
    listp = np.concatenate((list1,np.array([max]),np.flip(list1)))

    list2 = np.arange(0,min,-step)
    listn = np.concatenate((list2,np.array([min]),np.flip(list2)))

    try:
        match cycle:
            case '+': return listp
            case '-': return listn
            case '+-': return np.concatenate((listp,listn))
            case '-+': return np.concatenate((listn,listp))
    except:
        logger.critical('Invalid cycle type!')
        quit()
    
def timestamp():
    '''Returns timestamp'''
    import datetime
    import time
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S:%f')

def import_module(logger,type,srcmtr_model=None,measurement_type=None,plot_type=None):
    '''Imports a module from string'''
    import importlib
    logger.debug(f'Importing {type} module')
    try:
        match type:
            case 'sourcemeter':
                file_name = f'sourcemeters.{srcmtr_model}'
                obj_name = 'Sourcemeter'
            
            case 'measurement':
                file_name = f'measurements.{measurement_type}'
                obj_name = 'Measurement'

            
            case 'plot':
                file_name = f'plots.{plot_type}'
                obj_name = 'Plots'

        file = importlib.import_module(file_name)
        logger.debug(f'{file_name} module imported')
        obj = getattr(file, obj_name)
        logger.debug(f'{obj_name} class imported')
        return obj
    
    except:
        logger.critical(f'{type} could not be imported!')
        quit()