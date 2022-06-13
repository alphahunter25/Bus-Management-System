from rich.console import Console
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text


import os
os.system("cls")
console = Console()

menu = Table(title="Bus Management System", box = box.DOUBLE_EDGE)
menu.add_column("Key", style="cyan bold", justify="center")
menu.add_column("Command", style="white italic")

menu.add_row("1", "Book Ticket")
menu.add_row("2", "Cancel Ticket")

# console.print(menu)


# choice = Prompt.ask("Please enter your choice ")

panel = Panel(Text("Hello", justify="center", style = "bold white"))
console.print(panel)

texter = Text("hello hello", style = "bold yellow underline")
console.print(texter)