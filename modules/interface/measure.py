from rich.console import Console
from rich.layout import Layout
from rich.text import Text
from rich.table import Table
from datetime import datetime
import time

console = Console()
layout = Layout()

layout.split(
    Layout(name='header', size=3),
    Layout(ratio=1, name='value_log'),
    Layout(size=5, name='progress_bar'),
)


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
    