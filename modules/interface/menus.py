from rich.panel import Panel
from rich.prompt import Prompt
from modules.interface.options import main_options
from modules.common_utils import printnnewlines
import os
import time



def main_menu(console):
    '''Main menu'''

    options, num_options = main_options(), [str(i) for i in range(len(main_options()))]

    printnnewlines(3)
    console.print(Panel.fit("[bold]Main Menu[/bold]", border_style="green"))

    for i, option in enumerate(options):
        console.print(f'[bold]{i} - {option}[/bold]')


    selection = None
    while selection not in num_options:
        selection = Prompt.ask("Select an option:", choices=[str(i) for i in range(len(options))])

        if selection not in num_options:
            console.print("[red]Invalid selection, please try again![/red]")

    return list(options.items())[int(selection)][1]




def measurement_file_menu(console,logger,path='modules/measurements'):
    
    measurement_types = os.listdir(path)
    measurement_types = [filename.split('.')[0] for filename in measurement_types if filename.endswith('.py')]
    
    printnnewlines(3)
    if measurement_types:
        
        choices = list(map(str, range(len(measurement_types))))
        console.print(Panel.fit("[bold]Measurement selection menu[/bold]", border_style="green"))

        for choice in choices:
            console.print(f'[bold]{choice} - {measurement_types[int(choice)]}[/bold]')

        selection = None

        while selection not in choices:
            selection = Prompt.ask("Select an option:", choices=choices)
            
            if selection not in choices:
                logger.warning('Invalid selection, please try again!')

        return measurement_types[int(selection)]
    else:
        logger.error('No measurement types found!')
        time.sleep(2)












#Test    
if __name__ == "__main__":
    from rich.console import Console
    main_menu(Console())