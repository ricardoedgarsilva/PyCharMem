from rich.panel import Panel
from rich.prompt import Prompt

def main_menu(console):

    options = [
        'Select Measurement',
        'Print Available Adresses',
        'Edit Configuration',
        'Exit'
    ]

    choices = [str(i) for i in range(len(options))]

    console.print(Panel.fit("[bold]Main Menu[/bold]", border_style="green"))

    for choice in choices:
        console.print(f'[bold]{choice} - {options[int(choice)]}[/bold]')

    selection = None

    while selection not in choices:
        selection = Prompt.ask("Select an option:", choices=choices)
        
        if selection not in choices:
            console.print("[red]Invalid selection, please try again![/red]")

    match selection:
        case '0': return 'select_measurement'
        case '1': return 'check_adresses'
        case '2': return 'edit_config'
        case '3': return 'exit'

    
if __name__ == "__main__":
    from rich.console import Console
    main_menu(Console())