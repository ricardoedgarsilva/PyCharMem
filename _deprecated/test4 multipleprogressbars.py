from rich.progress import Progress
import time

n_cycles = 3
n_vals = 5

with Progress() as progress:
    value_task = progress.add_task(f"[purple]Value 0/{n_vals}", total=n_vals)  
    cycle_task = progress.add_task(f"[blue]Cycle 0/{n_cycles}", total=n_cycles)
    # iterate through cycles
    for i in range(1, n_cycles+1):
        for k in range(1, n_vals+1):
            progress.update(value_task, advance=1)
            time.sleep(1)
        progress.update(value_task, advance=-n_vals)   
        progress.update(cycle_task, advance=1, description=f"[blue]Cycle {i}/{n_cycles}")
