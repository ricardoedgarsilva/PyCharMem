from art import text2art
from rich.panel import Panel
from rich.prompt import Prompt

def main_menu(console):
    
    print(text2art("PyCharMem"))

    options = [
        'Select Measurement',
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

    return int(selection)

    
if __name__ == "__main__":
    from rich.console import Console
    main_menu(Console())