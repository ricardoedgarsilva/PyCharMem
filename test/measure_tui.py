from rich.console import Console
from rich.layout import Layout
from rich.text import Text
from rich.table import Table
from datetime import datetime
from rich.live import Live
import time

console = Console()
layout = Layout()

class measure_tui:
    def __init__(self,console,cycles):
        self.layout = Layout()

        self.layout.split(
            Layout(name='header', size=2),
            Layout(ratio=1, name='value_table'),
            Layout(size=5, name='console_log'))
        
        #split header into two columns, one for the time/date and the other for a progress bar
        self.layout['header'].split(
            Layout(name='time', size=3),
            Layout(name='progress', ratio=1))
        
        progress_bar = progress.add_task("Task name", total=100)

    #Create a function that updates all the elements of the layout
    def update_progress(self,console,layout,progress):
        p)
        layout['progress_bar'].update(progress)

    def update_layout(self,console,layout,data,progress):
        console.print(layout)
        layout['time'].update(Text(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        layout['progress_bar'].update(progress)
        







table = Table(title="Star Wars Movies")
table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")


layout['header'].update(Text(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
layout['value_log'].update(table)


console.print(layout)

for i in range(10):
    table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    layout.update(console)
    console.print(layout)
    time.sleep(1.5)
    