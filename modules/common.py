#This file contains simple functions used throughout the code

def clear_terminal():
    import os
    os.system('cls||clear')

def edit_config():
    import os
    os.startfile(r'config.ini')


def load_config():
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config