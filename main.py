from classes import *
from rich.console import Console
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
import os

os.system("cls")
console = Console()

panel = Panel(Text("Welcome to the Bus Management System." , justify="center", style = "bold white"))
console.print(panel)

useAdMenu = Table(title="Would you like to run this program as:", box = box.DOUBLE_EDGE, width=40)
useAdMenu.add_column("Key", style="cyan bold", justify="center", width = 1)
useAdMenu.add_column("Option", style="white italic")
useAdMenu.add_row("1", "A User")
useAdMenu.add_row("2", "An Admin")

console.print(useAdMenu)


useAd = Prompt.ask("Please enter your choice ")

if useAd == "1":
    print("so far so good")















