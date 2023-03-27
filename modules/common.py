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

def path_exists(path):
    import os
    return os.path.exists(path)

def get_path():
    import os
    return os.path.dirname(os.path.realpath(__file__))

