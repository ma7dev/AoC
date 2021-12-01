from rich import print
import time
def start_timer():
    globals()['start_time'] = time.time()
def end_timer():
    globals()['end_time'] = time.time()
def pprint(part,message):
    end_timer()
    print(f"[green]Part {part}[/green]: [italic yellow]{message}[/italic yellow] - [bold blue]{globals()['end_time'] - globals()['start_time']:0.4f}s[/bold blue]")
