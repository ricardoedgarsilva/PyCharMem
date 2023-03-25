from rich.panel import Panel
from rich.prompt import Prompt
import os
import time

def measurement_selection_menu(console,path='modules/measurements'):
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
                console.print("[red]Invalid selection, please try again![/red]")

        return int(selection)
    else:
        console.print('[bold][red]No measurement types found![/red][/bold]')
        time.sleep(2)




