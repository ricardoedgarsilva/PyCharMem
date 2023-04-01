from rich.panel import Panel
from rich.prompt import Prompt
from modules.common import printnewlines
import numpy as np
import os
import time
import inquirer


def menu(logger,console,type):
    '''Several Menus'''
    
    logger.debug(f'Menu called! Type: {type}')
    match type:
        case 'main':
            name = 'Main Menu'
            message = 'Select an option:'
            choices = ['Exit','Select Measurement','Print Available Addresses','Edit Configuration']
        
        case 'measurements':
            try:
                list_dir = os.listdir('measurements')
                measurement_types = [filename.split('.')[0] for filename in list_dir if filename.endswith('.py')]
                logger.debug(f'{len(measurement_types)} measurement types found')
            except:
                logger.critical('No measurement types found!')
                time.sleep(2)
                quit()

            name = 'Measurement Selection Menu'
            message = 'Select a measurement:'
            choices = measurement_types
            choices.append('Back')

    printnewlines(1)
    console.print(Panel.fit(f"[bold]{name}[/bold]", border_style="green"))
    menu = [inquirer.List('choice',message=message,choices=choices)]
    answer = inquirer.prompt(menu)
    logger.debug(f'Returning answer: {answer}')
    return answer['choice']


 
