from rich.panel import Panel
from rich.prompt import Prompt
import os
import time



def sel_menu(console,logger,path='modules/measurements'):
    measurement_types = os.listdir(path)


    if measurement_types:
        choices = [str(i) for i in range(len(measurement_types))]

        console.print(Panel.fit("[bold]Measurement selection menu[/bold]", border_style="green"))

        for choice in choices:
            console.print(f'[bold]{choice} - {measurement_types[int(choice)]}[/bold]')

        selection = None

        while selection not in choices:
            selection = Prompt.ask("Select an option:", choices=choices)
            
            if selection not in choices:
                logger.warning('Invalid selection, please try again!')

        print(f'You selected {measurement_types[int(selection)]}!')
        return measurement_types[int(selection)]
    else:
        logger.error('No measurement types found!')
        time.sleep(2)



