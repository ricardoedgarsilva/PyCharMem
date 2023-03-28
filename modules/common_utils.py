#This file contains simple functions used throughout the code

def printnnewlines(n):
    '''Prints n newlines'''
    print(n*'\n')

def splash_screen(console):
    '''Prints the splash screen'''
    import configparser
    from art import text2art

    info = configparser.ConfigParser()
    info.read('modules\\info.ini')
    print(text2art(info.get('main','name')))
    console.print(f"Version: {info.get('main','version')}",style='bold blue')
    console.print(f"Author: {info.get('main','author')}",style='bold blue')
    printnnewlines(5)

def clear_terminal():
    '''Clears the terminal'''
    import os
    os.system('cls||clear')

def edit_config(logger):
    '''Opens the config.ini file in the default text editor'''
    import os
    os.startfile(r'config.ini')
    logger.info('Config file opened!')


def load_config(logger):
    '''Returns the config object'''
    try:
        import configparser
        config = configparser.ConfigParser()
        config.read('config.ini')
        logger.info('Config file loaded!')
        return config
    except:
        logger.critical('Config file not found!')
        quit()

def path_exists(path):
    '''Returns True if the path exists, False otherwise'''
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

def create_path(path):
    '''Creates the path if it doesn't exist'''
    import os
    if path_exists(path):
        pass
    else:
        os.makedirs(path)

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

def print_available_addresses(console,logger):
    '''Prints the available adresses'''
    import pyvisa
    from rich.panel import Panel
    from modules.common_utils import printnnewlines

    rm = pyvisa.ResourceManager()
    printnnewlines(3)
    console.print(Panel.fit("[bold]Available Addresses[/bold]", border_style="green"))
    for address in rm.list_resources():
        console.print(address)
    
    if len(rm.list_resources()) == 0:
        logger.critical('No addresses found!')




def verbose_debug(verbose):
    '''Hides the debug messages'''
    from rich.logging import RichHandler
    import logging
    if verbose:
        logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    else:
        logging.basicConfig(level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])

    return logging.getLogger("rich")


def check_missing_params(my_dict, my_list, logger):
    '''Checks if the dictionary has all the keys in the list'''
    
    missing_items = [item for item in my_list if item not in my_dict]

    if len(missing_items) == 0:
        logger.info('All parameters found!')
    else:
        logger.critical('Missing parameters:')
        for item in missing_items:
            logger.critical(f'- {item}')
        quit()