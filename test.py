from rich.panel import Panel
from rich.console import Console

console = Console()
title = Panel.fit("My Title", border_style="green")
console.print(title)