#This file contains simple functions used throughout the code

def splash_screen(console):
    import configparser
    from art import text2art

    info = configparser.ConfigParser()
    info.read('modules\\info.ini')
    print(text2art(info.get('main','name')))
    console.print(f"Version: {info.get('main','version')}",style='bold blue')
    console.print(f"Author: {info.get('main','author')}",style='bold blue')
    print(5*'\n')

def clear_terminal():
    '''Clears the terminal'''
    import os
    os.system('cls||clear')

def edit_config():
    '''Opens the config.ini file in the default text editor'''
    import os
    os.startfile(r'config.ini')


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

def print_available_adresses(console):
    '''Prints the available adresses'''
    import pyvisa
    from rich.panel import Panel
    rm = pyvisa.ResourceManager()

    console.print(Panel.fit("[bold]Available Adresses[/bold]", border_style="green"))
    for adress in rm.list_resources():
        console.print(adress)



def hide_debug(config,logger):
    '''Hides the debug messages'''

    if not config.getboolean('general','verbose_debug'):
        logger.setLevel('INFO')