from rich.panel import Panel
from rich.prompt import Prompt
from modules.interface.options import main_options
from modules.common_utils import printnnewlines

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


    
if __name__ == "__main__":
    from rich.console import Console
    main_menu(Console())