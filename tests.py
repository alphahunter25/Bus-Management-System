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


panel = Panel(Text("Welcome to the Bus Management System." , justify="left", style = "bold cyan"))
console.print(panel)


