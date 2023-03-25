#This file contains simple functions used throughout the code

def clear_terminal():
    import os
    os.system('cls||clear')

def edit_config():
    import os
    os.startfile(r'config.ini')

def edit_config_new(console):
    import subprocess
    import time
    
    if subprocess.call(['open', '-a', 'TextEdit', r'config.ini']) == 0:
        console.print('[bold][green]File saved and closed.[/green][/bold]')
        time.sleep(2)
    else:
        console.print('[bold][red]Error opening file![/red][/bold]')
        time.sleep(2)


def load_config():
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config