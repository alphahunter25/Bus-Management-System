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

lahoreBranch = Branch("Lahore", 5000)

# useAd = Prompt.ask("Please enter your choice ")

# if useAd == "1":
# #     print("so far so good")
# mainchecker = False

# if

class Menu:
    def exiter(self):
        console.print(Text("Thank you for using the Bus Management System.", style = "bold red"))
        exit()

    def intro(self):
        panel = Panel(Text("Welcome to the Bus Management System." , justify="center", style = "bold cyan"))
        console.print(panel)

        useAdMenu = Table(title="Would you like to run this program as:", box = box.DOUBLE_EDGE, width=40)
        useAdMenu.add_column("Key", style="yellow bold", justify="center", width = 1)
        useAdMenu.add_column("Options", style="white italic")
        useAdMenu.add_row("1", "A User")
        useAdMenu.add_row("2", "An Admin")

        console.print(useAdMenu)
        useadPrompt = Prompt.ask("Please choose one of the options or press Q to quit ")
        if useadPrompt == "1" or useadPrompt == "2":
            return useadPrompt
        elif useadPrompt == "Q":
            self.exiter()
        else:
            console.print(Text("Please enter a valid option", style = "bold red"))
            return self.intro()

    def admin(self):
        os.system("cls")
        panel = Panel(Text("Running the program as an Admin" , justify="center", style = "bold cyan"))
        console.print(panel)


        adMenu = Table(title="Please choose one of the following commands", box = box.DOUBLE_EDGE, width=55)
        adMenu.add_column("Key", style="yellow bold", justify="center", width = 5)
        adMenu.add_column("Options", style="white italic")
        adMenu.add_row("1", "Change the fare of the First Class buses")
        adMenu.add_row("2", "View branch revenue")
        adMenu.add_row("3", "Add another route to this branch")  
        adMenu.add_row("4", "Clear the screen")
        adMenu.add_row("5", "Go back to the main menu")                

        console.print(adMenu)

        looper = True
        while looper:
            adPrompt = Prompt.ask("Please choose one of the options or press Q to quit ")

            if adPrompt == "1":
                newFare = Prompt.ask("Please enter the new fare ")
                for i in lahoreBranch.buses:
                    if i.busType == "First Class":
                        i.fare = newFare

            elif adPrompt == "2":
                revenuecalc = lahoreBranch.revenue 
                console.print(Text(f"This branch has made Rs{revenuecalc} since it was made.", style = "bold underline medium_spring_green"))

            elif adPrompt == "3":
                start = Prompt.ask("Please enter the starting point of the new route ")
                end = Prompt.ask("Please enter the destination of the new route ")
                fare = Prompt.ask("Please enter the fare of the new route ")
                time = Prompt.ask("Please enter the departure time of the new route ")

                newRoute = Route(start, end, fare, time)
                lahoreBranch.routes.append(newRoute)
                lahoreBranch.buses += Economy(newRoute)
                lahoreBranch.buses += FirstClass(newRoute, lahoreBranch.buses[1])

                console.print(Text(f"Route succesfully added", style = "bold underline medium_spring_green"))

            elif adPrompt == "Q" or adPrompt == "q":
                self.exiter()

            elif adPrompt == "4":
                # os.system("cls")
                return self.admin()

            elif adPrompt == "5":
                looper = False
                return False


            else:
                console.print(Text("Please enter a valid option", style = "bold red"))

    def user(self):
        panel = Panel(Text("Running the program as a User" , justify="center", style = "bold cyan"))
        console.print(panel)


        adMenu = Table(title="Please choose one of the following commands", box = box.DOUBLE_EDGE, width=55)
        adMenu.add_column("Key", style="yellow bold", justify="center", width = 5)
        adMenu.add_column("Options", style="white italic")
        adMenu.add_row("1", "Log in ")
        adMenu.add_row("2", "Create a new account")
        adMenu.add_row("3", "Go back to the main menu")  

        console.print(adMenu)

        adPrompt = Prompt.ask("Please choose one of the options or press Q to quit ")

        if adPrompt == "1":
            name = Prompt.ask("Please choose one of the options or press Q to quit ")









def main():
    # mainer = False
    menuinit = Menu()
    os.system("cls")
    introout = menuinit.intro()
    os.system("cls")
    menuout = menuinit.admin()
    if menuout == False:
        # mainer = True
        os.system("cls")
        main()

# main()
    # if introout == "2":
    #     os.system("cls")
    #     while mainchecker == False:
    #         menuinit.admin()



main()







    
















